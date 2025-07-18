import numpy as np
import xarray as xr
import pandas as pd
from params import *
from configuration import *
import jobtools
from pathlib import Path


# MAIA JOB
def process_maia(sub_key, **p):
    participant = sub_key
    path_maia = data_path / participant / 'questionnaires' / 'ses01' / f'maia_{participant}.xlsx'
    raw_maia = pd.read_excel(path_maia).reset_index() # load MAIA
    
    raw_maia_reversed  = raw_maia.copy()
    raw_maia_reversed['item'] = np.nan
    
    # reverse score where it has to be reversed (5 - score = reversing)
    for i, row in raw_maia.iterrows(): 
        if p['reverse'][row['question']] == '+': 
            raw_maia_reversed.loc[i, 'score'] = row['score']
        elif p['reverse'][row['question']] == '-':
            raw_maia_reversed.loc[i, 'score'] = 5 - row['score']
    
    raw_maia_reversed = raw_maia_reversed.set_index('question')
    
    maia_processed = pd.DataFrame(columns = p['items'].keys())
    
    for item, num_questions in p['items'].items(): # loop over items and corresponding num of questions ..
        maia_processed.loc[0,item] = np.mean(raw_maia_reversed.loc[num_questions, 'score']) # ... and average scores of questions and store it into dataframe
    
    maia_processed.insert(0 , 'participant', participant)

    return xr.Dataset(maia_processed)

def test_process_maia():
    sub_key = 'P01'
    ds = process_maia(sub_key, **maia_params)
    print(ds.to_dataframe())
    
maia_job = jobtools.Job(precomputedir, 'maia', maia_params, process_maia)
jobtools.register_job(maia_job)
    
    


# STAI LONG FORM JOB
def process_stai_longform(run_key, **p):
    participant, session = run_key.split('_')
    path_stai = data_path / participant / 'questionnaires' / session / f'stai_{session}_{participant}.xlsx'
    
    raw_stai = pd.read_excel(path_stai)
    
    # reverse scores if needed
    score_corrected = []
    for i, row in raw_stai.iterrows():
        if row['correction'] == '-':
            score_c = 5 - row['score']
        else : 
            score_c = row['score']
        score_corrected.append(score_c)

    etat = np.sum(score_corrected[0:20]) # state = sum of questions 0 to 19
    trait = np.sum(score_corrected[20:None]) # trait = sum of questions 20 to 39
    
    mean_etat = p['mean_etat']
    std_etat = p['sd_etat']
    mean_trait = p['mean_trait']
    std_trait = p['sd_trait']
    
    if etat > (mean_etat + 1.96 *std_etat):
        interpretation_etat = 'Etat anxieux'
    elif etat < (mean_etat-1.96*std_etat):
        interpretation_etat = 'Etat moins que anxieux'
    else :
        interpretation_etat = 'Etat dans les normes'
        
    if trait > (mean_trait+1.96*std_trait): 
        interpretation_trait = 'Trait anxieux'
    elif trait < (mean_trait-1.96*std_trait):
        interpretation_trait = 'Trait moins que anxieux'
    else : 
        interpretation_trait = 'Trait dans les normes'
    
    dict_results = {'participant':participant, 'session': session, 'etat': etat, 'trait':trait, 'interpretation_etat':interpretation_etat, 'interpretation_trait':interpretation_trait}
    return xr.Dataset(pd.DataFrame.from_dict(dict_results, orient = 'index').T)

def test_process_stai_longform():
    run_key = 'P01_ses01'
    ds = process_stai_longform(run_key, **stai_longform_params)
    print(ds.to_dataframe())
    
stai_longform_job = jobtools.Job(precomputedir, 'stai_longform', stai_longform_params, process_stai_longform)
jobtools.register_job(stai_longform_job)





# RELAXATION
def process_relaxation(sub_key, **p):
    """
    Just group raw data from multiple sessions (excel containing answers to questions)
    and rename columns
    """
    participant = sub_key
    
    keep_cols = ['eveil_brute','Caractère_relaxant_brute','Intensité_relaxation_brute','Longueur_session_brute']
    
    baseline_path = data_path / participant / 'questionnaires' / 'ses02' / f'cotations_BL_{participant}.xlsx'
    stim_path = data_path / participant / 'questionnaires' / 'ses02' / f'cotation_stim_{participant}.xlsx'
    
    baseline_df = pd.read_excel(baseline_path, index_col = 0)
    stim_df = pd.read_excel(stim_path, index_col = 0)
    
    concat = []
    for ses in session_keys:
        if ses == 'baseline':
            sel = baseline_df[keep_cols]
            sel.insert(0 , 'stim_name', np.nan)
            sel.insert(0 , 'session', ses)
            sel.insert(0, 'participant', participant)
        else:
            sel = stim_df.set_index('Stimulation').loc[ses,keep_cols].to_frame().T
            sel.insert(0 , 'stim_name', stim_df.set_index('Stimulation').loc[ses,'name'])
            sel.insert(0 , 'session', ses)
            sel.insert(0, 'participant', participant)
        concat.append(sel)
        
    rename_col = {'eveil_brute':'Arousal',
                  'Caractère_relaxant_brute':'Relaxation',
                  'Intensité_relaxation_brute':'Relaxation_intensity',
                  'Longueur_session_brute':'Perceived_duration'}
    
    df_return = pd.concat(concat).reset_index(drop = True).rename(columns = rename_col)
    df_return['Perceived_duration'] = 100 - df_return['Perceived_duration'].values
    
    return xr.Dataset(df_return)

def test_process_relaxation():
    sub_key = 'P01'
    ds = process_relaxation(sub_key, **relaxation_params)
    print(ds.to_dataframe())
    
relaxation_job = jobtools.Job(precomputedir, 'relaxation', relaxation_params, process_relaxation)
jobtools.register_job(relaxation_job)


###
# RELAXATION
def process_emotions(sub_key, **p):
    participant = sub_key
    session_keys = ['odor','music']
    
    keep_cols = ['intensité_brute','hédonicité_brute','Evocation_souvenirs_brute','Caractère_irritant_brute','Valence_émotionnelle_brute','Intensité_émotionnelle_brute']

    stim_path = data_path / participant / 'questionnaires' / 'ses02' / f'cotation_stim_{participant}.xlsx'
    
    stim_df = pd.read_excel(stim_path, index_col = 0)
    
    concat = []
    for ses in session_keys:
        sel = stim_df.set_index('Stimulation').loc[ses,keep_cols].to_frame().T
        sel.insert(0 , 'stim_name', stim_df.set_index('Stimulation').loc[ses,'name'])
        sel.insert(0 , 'session', ses)
        sel.insert(0, 'participant', participant)
        concat.append(sel)
        
    rename_col = {'intensité_brute':'Intensity',
                  'hédonicité_brute':'Hedonicity',
                  'Evocation_souvenirs_brute':'Memories',
                  'Caractère_irritant_brute':'Irritability',
                 'Valence_émotionnelle_brute':'Emotional_Valence',
                 'Intensité_émotionnelle_brute':'Emotional_Intensity'}
    
    df_return = pd.concat(concat).reset_index(drop = True).rename(columns = rename_col)
    
    return xr.Dataset(df_return)

def test_process_emotions():
    sub_key = 'P01'
    ds = process_emotions(sub_key, **emotions_params)
    print(ds.to_dataframe())
    
emotions_job = jobtools.Job(precomputedir, 'emotions', emotions_params, process_emotions)
jobtools.register_job(emotions_job)


###
# OAS
def process_oas(sub, **p):
    file = data_path / sub / 'questionnaires' / 'ses02' / f'OAS_session2_{sub}.xlsx'
    df = pd.read_excel(file)
    scores_corrected = []
    for i , row in df.iterrows():
        if row['correction'] == '-':
            scores_corrected.append(6 - row['score'])
        else:
            scores_corrected.append(row['score'])
    mean = np.mean(scores_corrected)
    df_return = pd.Series()
    df_return['participant'] = sub
    df_return['OAS'] = mean
    return xr.Dataset(df_return.to_frame().T)

def test_process_oas():
    sub = 'P01'
    ds = process_oas(sub, **oas_params)
    print(ds.to_dataframe())
    
oas_job = jobtools.Job(precomputedir, 'oas', oas_params, process_oas)
jobtools.register_job(oas_job)

###
# BMRQ
def process_bmrq(sub, **p):
    file = data_path / sub / 'questionnaires' / 'ses02' / f'BMRQ_session2_{sub}.xlsx'
    df = pd.read_excel(file)
    scores_corrected = []
    for i , row in df.iterrows():
        if row['correction'] == '-':
            scores_corrected.append(6 - row['score'])
        else:
            scores_corrected.append(row['score'])
    mean = np.mean(scores_corrected)
    df_return = pd.Series()
    df_return['participant'] = sub
    df_return['BMRQ'] = mean
    return xr.Dataset(df_return.to_frame().T)

def test_process_bmrq():
    sub = 'P01'
    ds = process_bmrq(sub, **bmrq_params)
    print(ds.to_dataframe())
    
bmrq_job = jobtools.Job(precomputedir, 'bmrq', bmrq_params, process_bmrq)
jobtools.register_job(bmrq_job)


###

def compute_all():
    # jobtools.compute_job_list(maia_job, subject_keys, force_recompute=False, engine='loop')
    # jobtools.compute_job_list(stai_longform_job, run_keys_stai, force_recompute=False, engine='loop')
    # jobtools.compute_job_list(relaxation_job, subject_keys, force_recompute=False, engine='loop')
    # jobtools.compute_job_list(emotions_job, subject_keys, force_recompute=False, engine='loop')
    jobtools.compute_job_list(oas_job, subject_keys, force_recompute=False, engine='loop')
    # jobtools.compute_job_list(bmrq_job, subject_keys, force_recompute=False, engine='loop')



if __name__ == '__main__':
    # test_process_maia()
    # test_process_stai_longform()
    test_process_relaxation()
    # test_process_emotions()
    # test_process_oas()
    # test_process_bmrq()
    # compute_all()