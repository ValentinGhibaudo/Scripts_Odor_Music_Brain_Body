# RUN KEYS

from configuration import data_path

subject_keys = ['P01','P02','P03','P04','P05',
                'P06','P07','P08','P09','P10',
                'P11','P12','P13','P14','P15',
                'P16','P17','P18','P19','P20',
                'P21','P23','P24','P25', # P22 not in list because artifacted
                'P26','P27','P28','P29','P30','P31'] 

session_keys = ['baseline','music','odor']

run_keys = [f'{sub_key}_{ses_key}' for sub_key in subject_keys for ses_key in session_keys]

baseline_keys = [f'{sub_key}_baseline' for sub_key in subject_keys]
stim_keys = [f'{sub_key}_{stim_key}' for sub_key in subject_keys for stim_key in ['music','odor']]

run_keys_stai = [f'{sub_key}_{ses_key}' for sub_key in subject_keys for ses_key in ['ses01','ses02']]

global_key = 'all'

music_mapper = {
        1:'1_Classic',
          2:'2_Electro',
          3:'3_Hard_rock',
          4:'4_Jazz',
          5:'5_Metal',
          6:'6_Pop',
          7:'7_Raga',
          8:'8_RAP_1',
        9:'9_RAP_2',
          10:'10_Variété',
         }

tempos = {1:55,
          2:128,
          3:110,
          4:122,
          5:134,
          6:60,
          7:56,
          8:68,
          9:108,
          10:81,
         }

chosen_musics = {'P01': 10,
 'P02': 10,
 'P03': 10,
 'P04': 3,
 'P05': 9,
 'P06': 4,
 'P07': 7,
 'P08': 10,
 'P09': 9,
 'P10': 9,
 'P11': 10,
 'P12': 10,
 'P13': 9,
 'P14': 7,
 'P15': 8,
 'P16': 10,
 'P17': 10,
 'P18': 8,
 'P19': 10,
 'P20': 5,
 'P21': 10,
 'P23': 8,
 'P24': 6,
 'P25': 5,
 'P26': 9,
 'P27': 9,
 'P28': 9,
 'P29': 9,
 'P30': 5,
 'P31': 10
                }

répondeurs_resp = {'P01': 'non_répondeur', # those who increase cycle freq during music AND decrease cycle freq during odor = 16 répondeurs, 14 non répondeurs
                     'P02': 'répondeur',
                     'P03': 'non_répondeur',
                     'P04': 'répondeur',
                     'P05': 'répondeur',
                     'P06': 'répondeur',
                     'P07': 'répondeur',
                     'P08': 'répondeur',
                     'P09': 'non_répondeur',
                     'P10': 'répondeur',
                     'P11': 'répondeur',
                     'P12': 'non_répondeur',
                     'P13': 'non_répondeur',
                     'P14': 'répondeur',
                     'P15': 'non_répondeur',
                     'P16': 'non_répondeur',
                     'P17': 'non_répondeur',
                     'P18': 'répondeur',
                     'P19': 'non_répondeur',
                     'P20': 'répondeur',
                     'P21': 'non_répondeur',
                     'P23': 'non_répondeur',
                     'P24': 'non_répondeur',
                     'P25': 'répondeur',
                     'P26': 'répondeur',
                     'P27': 'répondeur',
                     'P28': 'répondeur',
                     'P29': 'non_répondeur',
                     'P30': 'répondeur',
                     'P31': 'non_répondeur'
                  }


# REREF
reref = 'average'

if reref == None:
    eeg_chans = ['Fp1', 'Fz', 'F3', 'F7', 'FT9', 'FC5', 'FC1', 'C3', 'T7', 
             'TP9','CP5','CP1', 'Pz', 'P3', 'P7', 'O1', 'Oz', 'O2', 'P4', 
             'P8', 'TP10', 'CP6','CP2', 'C4', 'T8', 'FT10', 'FC6', 'FC2', 'F4', 'F8', 'Fp2']
else:
    eeg_chans = ['Fp1', 'Fz', 'F3', 'F7', 'FT9', 'FC5', 'FC1', 'C3', 'T7', 
             'TP9','CP5','CP1', 'Pz', 'P3', 'P7', 'O1', 'Oz', 'O2', 'P4', 
             'P8', 'TP10', 'CP6','CP2', 'C4', 'T8', 'FT10', 'FC6', 'FC2', 'F4', 'F8', 'Fp2','Cz']


# USEFUL LISTS & DICTS


bio_chans = ['ECG','RespiNasale','RespiVentrale','GSR']

all_chans = ['Fp1', 'Fz', 'F3', 'F7', 'FT9', 'FC5', 'FC1', 'C3', 'T7', 'TP9',
             'CP5','CP1', 'Pz', 'P3', 'P7', 'O1', 'Oz', 'O2', 'P4', 'P8', 'TP10',
             'CP6','CP2', 'C4', 'T8', 'FT10', 'FC6', 'FC2', 'F4', 'F8', 'Fp2',
             'ECG','RespiNasale','RespiVentrale','GSR','FCI']

participants_label = {
    'P01':'DB01', # OK
    'P02':'FB02', # OK
    'P03':'ZB03', # OK
    'P04':'EM04', # OK
    'P05':'TM05', # OK
    'P06':'AC06', # OK
    'P07':'CB07', # OK
    'P08':'ZB08', # OK
    'P09':'MA09', # OK
    'P10':'AA10', # OK
    'P11':'MB11', # OK
    'P12':'AP12', # OK
    'P13':'ZC13', # OK
    'P14':'FC14', # OK
    'P15':'AP15', # OK
    'P16':'EP16', # OK
    'P17':'AG17', # OK
    'P18':'MP18', # OK
    'P19':'SR19', # OK
    'P20':'MV20', # OK
    'P21':'GA21', # OK
    'P22':'SB22', # OK
    'P23':'PB23', # OK
    'P24':'MB24', # OK
    'P25':'MB25', # OK
    'P26':'EZ26', # OK
    'P27':'AM27', # OK
    'P28':'MC28', # OK
    'P29':'ML29', # OK
    'P30':'EG30', # OK
    'P31':'MG31' # OK
    }


session_duration = 600.


#### PROCESSING PARAMS
srate = 1000

fbands = {
    'delta':[1,4],
    'theta':[4,8],
    'alpha':[8,12],
    'beta':[12,30],
    'low_gamma':[30,45],
    'high_gamma':[55,100], 
    'very_high_gamma':[100,200],
    }

ecg_inversion = { 
'P01':1, # OK
'P02':1, # OK
'P03':-1, # OK
'P04':-1, # OK
'P05':-1,  # OK
'P06':-1, # OK
'P07':1, # OK
'P08':-1, # OK
'P09':-1, # OK
'P10':-1, # OK
'P11':1, # OK
'P12':-1, # OK
'P13':-1, # OK
'P14':-1, # OK
'P15':1, # OK
'P16':-1, # OK
'P17':1, # OK
'P18':-1, # OK
'P19':-1, # OK
'P20':-1, # OK 
'P21':-1, # OK
'P22':-1, # OK
'P23':1, # OK
'P24':-1, # OK
'P25':-1, # Ok
'P26':-1, # OK
'P27':-1, # OK
'P28':-1, # OK
'P29':-1, # OK
'P30':-1, # OK
'P31':-1 # OK        
}



## ICA : 
n_components_decomposition = 10

# components exclusion
ica_excluded_component = {
'P01':{'baseline':[0,1],'music':[0,1],'odor':[0,1]}, # OK
'P02':{'baseline':[0,1],'music':[0,3],'odor':[0,2]}, # OK
'P03':{'baseline':[0,2],'music':[0,1],'odor':[1,3]}, # OK
'P04':{'baseline':[5],'music':[5],'odor':[0,4]}, # OK
'P05':{'baseline':[0],'music':[0],'odor':[0]}, # OK
'P06':{'baseline':[1,3],'music':[1,3],'odor':[2,4]}, # OK
'P07':{'baseline':[1],'music':[3],'odor':[3]}, # OK
'P08':{'baseline':[1,3],'music':[0,2],'odor':[0,2]}, # OK
'P09':{'baseline':[1,2],'music':[1,3],'odor':[1,2]}, # OK
'P10':{'baseline':[0,1],'music':[0,1],'odor':[0,1]}, # OK
'P11':{'baseline':[0,4],'music':[0,4],'odor':[0,6]}, # OK
'P12':{'baseline':[0,1],'music':[0,1],'odor':[0,1]}, # OK 
'P13':{'baseline':[0,2],'music':[0,1],'odor':[0,1]}, # OK
'P14':{'baseline':[0,5],'music':[0,5],'odor':[0,2]}, # OK
'P15':{'baseline':[0,4],'music':[0,1,4],'odor':[0,2]}, # OK
'P16':{'baseline':[0,2],'music':[0,1],'odor':[0,1]}, # OK
'P17':{'baseline':[3,4],'music':[3,4],'odor':[1,2]}, # OK
'P18':{'baseline':[0,1,2],'music':[0,2],'odor':[0,2]}, # OK
'P19':{'baseline':[0,2],'music':[0,2],'odor':[0,2]}, # OK
'P20':{'baseline':[0,3],'music':[0,2],'odor':[0,4]}, # OK
'P21':{'baseline':[0,1],'music':[0,2],'odor':[0,1]}, # OK
'P22':{'baseline':[0,6],'music':[0,2],'odor':[0,4]}, # OK
'P23':{'baseline':[0,1],'music':[0,1],'odor':[0,1]}, # OK
'P24':{'baseline':[1,3],'music':[1,2],'odor':[2,3]}, # OK
'P25':{'baseline':[0,2],'music':[0,3],'odor':[0,2]}, # OK
'P26':{'baseline':[0,2],'music':[0,2],'odor':[0,2]}, # OK
'P27':{'baseline':[0,4],'music':[0,6],'odor':[0,2]}, # OK
'P28':{'baseline':[0],'music':[0,2],'odor':[0,2]}, # OK
'P29':{'baseline':[2],'music':[2],'odor':[1]}, # OK
'P30':{'baseline':[0,1],'music':[0,1],'odor':[0,1]}, # OK
'P31':{'baseline':[0,2],'music':[0,2],'odor':[0,2]} # OK
}

bio_filters = {
    'ECG':{'low':5,'high':45, 'ftype':'bessel', 'order':5} , 
    'RespiNasale':{'low':0.02, 'high':1.5, 'ftype':'butter', 'order':5} , 
    'RespiVentrale':{'low':0.02, 'high':1.5, 'ftype':'butter', 'order':5} , 
    'GSR':{'low':None, 'high':3, 'ftype':'butter', 'order':5}
}


## ANALYSES

## job params

import numpy as np

convert_vhdr_params = {
    'participants_label': participants_label,  
}

random_state = 27
notch_freqs = np.arange(50, 200, 50).tolist()
n_components_decomposition = 10

ica_figure_params = {
     'random_state' : random_state,
     'notch_freqs' : notch_freqs,
     'n_components_decomposition' : n_components_decomposition,
}

preproc_params = {
    'participants_label': participants_label,
    'notch_freqs' : notch_freqs,
    'save_ica_fig': True,
    'random_state' : random_state,
    'ica_excluded_component': ica_excluded_component,
    # 'eeg_chans': eeg_chans ,
    'n_components_decomposition' :n_components_decomposition ,
    'session_duration':session_duration,
    'lowcut':0.05, # lowcut frequency in Hz
    'highcut':200, # highcut frequency in Hz
    'ftype':'butter',
    'order':6,
    'reref':reref
}

artifact_params = {
    'preproc_params':preproc_params,
    'n_deviations':3, # number of deviations (MAD) to the median
    'window_size':1.5, # size in seconds of th moving window of rms
    'step': 0.5, # step time in second to compute rms windows
    'lf':30, # low cutoff frequency to filter signal on which artifacts are detected
    'hf':150, # high cutoff frequency to filter signal on which artifacts are detected
    'n_chan_artifacted':5 # when this number of channels are bugging at the same time, an artifact is detected
}

artifact_by_chan_params = {
    'preproc_params':preproc_params,
    'n_deviations':4.5, # number of deviations (MAD) to the median
    'window_size':1.5, # size in seconds of th moving window of rms
    'step': 0.5, # step time in second to compute rms windows
    'lf':30, # low cutoff frequency to filter signal on which artifacts are detected
    'hf':150, # high cutoff frequency to filter signal on which artifacts are detected
}

interp_artifact_params = {
    'artifact_params':artifact_params,
    'freq_min':30., # lowcut of frequency band to compute average power of whole signal to colour white noise before inserting in artifacted zones
    'margin_s':0.2, # duration of margins in seconds at the edge of artifact zones to smooth transition between real and patched signal
    'seed':None
}

count_artifact_params = {
    'artifact_params':artifact_params,
    'session_duration':session_duration,
    'thresh_prop_time_artifacted':0.3 # trials with more than this proportion of time artifacted will be marked as removable
}

respiration_features_params = {
    'inspiration_sign' : '+',
    'session_duration':session_duration
}


ecg_params = {
    'session_duration':session_duration,
    'ecg_inversion' : ecg_inversion,
    'thresh':5 # N mads to detect ECG peaks
}

rri_signal_params = {
    'ecg_params' : ecg_params,
    'max_interval' : 120, # in bpm
    'min_interval': 30., # in bpm
    'interpolation_kind': 'cubic', # interpolation of RRI signal as cubic or linear to get heart rate signal
}


psd_params = {
    'interp_artifact_params':interp_artifact_params,
    'lowest_freq':0.1, # lowest frequency interpretable in PSD = at least 5 cycles of this frequency in each Hann window
}

psd_bandpower_params = {
    'interp_artifact_params':interp_artifact_params,
    'lowest_freq':1, # lowest frequency interpretable in PSD = at least 5 cycles of this frequency in each Hann window
}

psd_baselined_params = {
'psd_bandpower_params':psd_bandpower_params}

bandpower_params = {
    'psd_baselined_params':psd_baselined_params,
    'fbands':fbands,
    'total_band':[psd_bandpower_params['lowest_freq'] , 200], # keep clean freq band (> 200 Hz = noisy)
}

power_at_resp_params = {
    'psd_params':psd_params,
    'session_duration':session_duration,
    'resp_chan':'RespiNasale',
    'lowest_freq_psd_resp':0.1, # lowest frequency interpretable in PSD = at least 5 cycles of this frequency in each Hann window
}

coherence_params = {
    'interp_artifact_params':interp_artifact_params,
    'resp_chan':'RespiNasale',
    'lowest_freq_psd_resp':0.15, # lowest frequency interpretable in coherence = at least 5 cycles of this frequency in each window
    'lowest_freq_coherence':0.15, # lowest frequency interpretable in coherence = at least 5 cycles of this frequency in each window
    'nfft_factor':2, # zero padding = window length * nfft_factor
    'n_cycles':4, # at least 'n_cycles' cycles of lowest frequency in each window
    'session_duration':session_duration
}

coherence_at_resp_params = {
    'coherence_params': coherence_params,
}

power_params = {
    'interp_artifact_params':interp_artifact_params,
    'chans':['F3','F4','C3','C4','T7','T8','P7','P8','O1','O2','Fz','Pz','Oz'],
    'decimate_factor':10, # down sampling power maps with this factor to reduce computation time / storage size
    'n_freqs':150, # number of frequency bins
    'f_start':4, # lowest frequency of time-frequency maps (logarithm increase then)
    'f_stop':150, # highest frequency of time-frequency maps (logarithm increase before)
    'c_start':10, # start number of oscillations of wavelets (for the f_start, logarithmically increasing)
    'c_stop':30, # stop number of oscillations of wavelets (for the f_stop, logarithmically increasing)
    'amplitude_exponent':2 # exponent to transform amplitude into power
}

baseline_params = {'power_params':power_params}


phase_freq_params = {
    'power_params':power_params,
    'respiration_features_params':respiration_features_params,
    'baseline_params':baseline_params,
    'n_phase_bins':200, # number of phase bins in phase frequency maps
    'segment_ratios':0.4, # ratio inspi / expi standardized
    'compress_cycle_modes':[0.1,0.2,0.25,0.3,0.4,0.5,0.6,0.7,0.75,0.8,0.9,10] # 10 = 'mean', rest = quantiles
}

phase_freq_concat_params = {
    'sub_keys':subject_keys,
    'ses_keys':session_keys,
    'chans':eeg_chans,
    'phase_freq_params':phase_freq_params,
    'baseline_mode':'rz_score', # baseline mode = robust zscore (rz_score) or z-score (z_score)
    'compress_cycle_modes':phase_freq_params['compress_cycle_modes'],
    'max_freq':20 # zoom frequency vector lower that 'max_freq'
}

phase_freq_fig_params = {
    'phase_freq_concat_params':phase_freq_concat_params,
    'chans':eeg_chans,
    'segment_ratios':phase_freq_params['segment_ratios'],
    'baseline_mode':phase_freq_concat_params['baseline_mode'],
    'compress_cycle_modes':phase_freq_params['compress_cycle_modes'],
    'delta_colorlim':0.01, # saturation of time-freq figure colors according to the 'delta_colorlim' to 1 - 'delta_colorlim' range
    'compress_subject':'Mean', # Mean or Median or q75
    'max_freq':phase_freq_concat_params['max_freq'], # zoom frequency vector
    'cmap':'viridis', # colormap of phase freq figures
    'quantile_by_subject_fig':0.75, # quantile to compress cycle axis
    'cluster_based_pval':0.05 # pvalue threshold to display significant time-freq points via cluster based permutations statistics
}

erp_time_freq_params = {
    'baseline_params':baseline_params,
    'power_params':power_params,
    'half_window_duration':5, # half size of windows in seconds
    'compress_cycle_mode':0.75 # quantile to compress cycle axis
}

erp_time_freq_concat_params = {
    'sub_keys':subject_keys,
    'ses_keys':session_keys,
    'erp_time_freq_params':erp_time_freq_params,
    'baseline_mode':'rz_score', # baseline method
    'center':'expi_time', # respi timestamp at the center of the windowed time-frequency maps
    'max_freq':phase_freq_concat_params['max_freq'] # zoom frequency vector below this frequency
}

erp_fig_params = {
    'erp_time_freq_concat_params':erp_time_freq_concat_params,
    'chans':eeg_chans,
    'baseline_mode':erp_time_freq_concat_params['baseline_mode'],
    'delta_colorlim':0.01, # saturation of time-freq figure colors according to the 'delta_colorlim' to 1 - 'delta_colorlim' range
    'max_freq':erp_time_freq_concat_params['max_freq'], # zoom frequency vector below this frequency
    'cmap':'viridis' # colormap used for time freq figures
}

time_phase_fig_params = {
    'phase_freq_concat_params':phase_freq_concat_params,
    'erp_time_freq_concat_params':erp_time_freq_concat_params,
    'chans':eeg_chans,
    'segment_ratios':phase_freq_params['segment_ratios'],
    'baseline_mode':phase_freq_concat_params['baseline_mode'],
    'compress_cycle_modes':phase_freq_params['compress_cycle_modes'],
    'delta_colorlim':0.01, # saturation of time-freq figure colors according to the 'delta_colorlim' to 1 - 'delta_colorlim' range
    'min_freq':6, # low cutoff frequency to zoom in frequency vector to construct figs
    'max_freq':14, # high cutoff frequency to zoom in frequency vector to construct figs
    'cmap':'viridis', # colormap used for time freq figures
    'cluster_based_pval':0.05, # pvalue threshold to display significant clusters time-freq points via clusted based permutation statistics
    'find_cluster_pval':0.04, # pvalue to find significantly large enough clusters of time-freq points
    'cluster_tail':-1 # one sided (-1 or +1) or two sided (0)
}

global_just_phase_fig_params =   { 'phase_freq_concat_params':phase_freq_concat_params,
    'chans':eeg_chans,
    'segment_ratios':phase_freq_params['segment_ratios'],
    'baseline_mode':phase_freq_concat_params['baseline_mode'],
    'compress_cycle_modes':phase_freq_params['compress_cycle_modes'],
    'delta_colorlim':0.01, # saturation of time-freq figure colors according to the 'delta_colorlim' to 1 - 'delta_colorlim' range
    'min_freq':6,# low cutoff frequency to zoom in frequency vector to construct figs
    'max_freq':14, # high cutoff frequency to zoom in frequency vector to construct figs
    'cmap':'viridis', # colormap used for time freq figures
    'cluster_based_pval':0.05, # pvalue threshold to display significant clusters time-freq points via clusted based permutation statistics
    'find_cluster_pval':0.04, # pvalue to find significantly large enough clusters of time-freq points
    'cluster_tail':-1 # one sided (-1 or +1) or two sided (0)
}

time_phase_chan_average_params = {
    'phase_freq_concat_params':phase_freq_concat_params,
    'erp_time_freq_concat_params':erp_time_freq_concat_params,
    'chans':eeg_chans,
    'segment_ratios':phase_freq_params['segment_ratios'],
    'baseline_mode':phase_freq_concat_params['baseline_mode'],
    'compress_cycle_modes':phase_freq_params['compress_cycle_modes'],
    'delta_colorlim':0.01,# saturation of time-freq figure colors according to the 'delta_colorlim' to 1 - 'delta_colorlim' range
    'min_freq':6,# low cutoff frequency to zoom in frequency vector to construct figs
    'max_freq':14, # high cutoff frequency to zoom in frequency vector to construct figs
    'cmap':'viridis',# colormap used for time freq figures
    'cluster_based_pval':0.05,# pvalue threshold to display significant clusters time-freq points via clusted based permutation statistics
    'find_cluster_pval':0.05, # pvalue to find significantly large enough clusters of time-freq points
    'cluster_tail':0  # one sided (-1 or +1) or two sided (0)
}

eda_params = {
    'session_duration':session_duration
}

rsa_params = {
    'respiration_features_params':respiration_features_params,
    'ecg_params':ecg_params,
    'n_phase_bins':100, # number of phase bins
}

stai_longform_params = {
    'mean_etat':35.4, # mean expected state anxienty in global population
    'mean_trait':34.8, # mean expected trait anxienty in global population
    'sd_etat':10.5, # sd expected state anxienty in global population
    'sd_trait':9.2 # sd expected trait anxienty in global population
}

maia_params = {
    'reverse':{1:'+',2:'+',3:'+',4:'+',5:'-',6:'-',7:'-',8:'-',9:'-',10 :'+',
               11:'+', 12:'+', 13:'+', 14:'+',15:'+',16:'+', 17:'+', 18:'+', 19:'+',20:'+',
               21:'+', 22:'+', 23:'+', 24:'+',25:'+',26:'+', 27:'+', 28:'+', 29:'+',30:'+',
               31:'+', 32:'+'}, # reverse questions (5 - score) if '-'
    'items':{ # grouping of questions and their label
        'noticing':[1,2,3,4],
        'not_distracting':[5,6,7],
        'not_worrying':[8,9,10],
        'attention_regulation':[11,12,13,14,15,16,17],
        'emotional_awareness':[18,19,20,21,22],
        'self_regulation':[23,24,25,26],
        'body_listening':[27,28,29],
        'trusting':[30,31,32],
    }
    }

relaxation_params = {}

emotions_params = {}

oas_params = {}
bmrq_params = {}

cycle_signal_params = {
    'interp_artifact_params':interp_artifact_params,
    'respiration_features_params':respiration_features_params,
    'n_phase_bins':1000, # number of phase bins
    'segment_ratios':0.4, # standardized ratio inspi / expi
    'chans':eeg_chans,
    'session_duration':session_duration
}

cycle_signal_modulation_params = {
    'cycle_signal_params':cycle_signal_params,
}

erp_signal_params = {
    'interp_artifact_params':interp_artifact_params,
    'respiration_features_params':respiration_features_params,
    'chans':eeg_chans,
    'session_duration':session_duration,
    'window_size_secs':10,
    'start_window_size_before_transition_secs':5,
}

concat_erp_signal_params = {
    'erp_signal_params':erp_signal_params
}


# Global concat of dataframes jobs params
# odor_rating_params = {'subject_keys':subject_keys,
#                      'date_of_data_generation':'06-06-2023',
#                     'rename_cols':{
#                         'odeur_name':'Odor_Name',
#                         'odeur_label':'Odor_Label',
#                         'appréciation_absolue_normalisée':'Absolute Hedonicity',
#                          'appréciation_relative_normalisée':'Hedonicity',
#                        'intensité_émotionnelle_relative_normalisée':'Emotional Intensity',
#                          'familiarité_relative_normalisée':'Familiarity',
#                            'intensité_relative_normalisée':'Stimulus Intensity',
#                            'evocation_relative_normalisée':'Memory Evocation'}
#                      }

eda_concat_params = {'run_keys':run_keys,
                    'eda_params':eda_params
                    }

hrv_concat_params = {'run_keys':run_keys,
                    'ecg_params':ecg_params,
                    }


rsa_concat_params = {'run_keys':run_keys,
                    'rsa_params':rsa_params,
                    }

bandpower_concat_params = {'run_keys':stim_keys,
                           'bandpower_params':bandpower_params
                          }

coherence_at_resp_concat_params = {'run_keys':run_keys,
                           'coherence_params':coherence_params
                          }
         
                           
power_at_resp_concat_params = {'run_keys':run_keys,
                           'power_at_resp_params':power_at_resp_params
                          }


resp_features_concat_params = {'run_keys':run_keys,
                           'respiration_features_params':respiration_features_params
                          }


relaxation_concat_params = {'run_keys':subject_keys,
                           'relaxation_params':relaxation_params
                          }

maia_concat_params = {'subject_keys':subject_keys,
                     'maia_params':maia_params
                     }

# stai_long_concat_params = {'run_keys':run_keys,
#                            'stai_longform_params':stai_longform_params
#                           }


modulation_cycle_signal_concat_params = {'run_keys':run_keys,
                           'cycle_signal_modulation_params':cycle_signal_modulation_params
                          }


oas_concat_params = {'run_keys':subject_keys,
                           'oas_params':oas_params
                          }

bmrq_concat_params = {'run_keys':subject_keys,
                           'bmrq_params':bmrq_params
                          }

cycle_signal_frames_params = {
    'cycle_signal_params':cycle_signal_params,
    'chan_line_signal':'Cz', # eeg chan for example line signal
    'resp_chan':'resp_nose'  # respi chan for example line signal
}

video_params = {'step':5, # down sampling frames by this factor
                'video_duration':30 # total video duration in seconds
               }

slope_params = {
    'power_params':power_params
}

deform_slope_params = {
    'slope_params':slope_params,
    'respiration_features_params':respiration_features_params,
    'n_phase_bins':1000, # number of phase bins
    'segment_ratios':0.4, # standardized ratio inspi / expi
}

individual_slope_fig_params = {
    'deform_slope_params':deform_slope_params
}