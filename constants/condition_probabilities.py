try:
    from type_constants import SubAdmissionTypes
except ModuleNotFoundError:
    from .type_constants import SubAdmissionTypes

condition_age_probability_dict = {

    SubAdmissionTypes.CANCER.name: {
        "Bladder Cancer": [((0, 10), 0.0),
                           ((11, 17), 0.00018),
                           ((18, 25), 0.0002),
                           ((25, 34), 0.00224),
                           ((35, 44), 0.00448),
                           ((45, 59), 0.00673),
                           ((45, 54), 0.00897),
                           ((55, 64), 0.02018),
                           ((65, 75), 0.02242),
                           ((76, 80), 0.0426)],  # AVG 0.00108
        "Brain and Nervous System Cancers": [((0, 10), 0.0),
                                             ((11, 17), 0.00023),
                                             ((18, 25), 0.00026),
                                             ((25, 34), 0.00291),
                                             ((35, 44), 0.00581),
                                             ((45, 59), 0.00872),
                                             ((45, 54), 0.01163),
                                             ((55, 64), 0.02616),
                                             ((65, 75), 0.02906),
                                             ((76, 80), 0.05522)],  # AVG 0.014
        "Breast Cancer": [((0, 10), 0.0),
                          ((11, 17), 0.00228),
                          ((18, 25), 0.00256),
                          ((25, 34), 0.02847),
                          ((35, 44), 0.05695),
                          ((45, 59), 0.11389),
                          ((45, 54), 0.11389),
                          ((55, 64), 0.25625),
                          ((65, 75), 0.28473),
                          ((76, 80), 0.54098)],  # AVG 0.14
        "Cervical Cancer": [((0, 10), 0.0),
                            ((11, 17), 0.000001),
                            ((18, 25), 0.000001),
                            ((25, 34), 0.00005),
                            ((35, 44), 0.00032),
                            ((45, 59), 0.00064),
                            ((45, 54), 0.00064),
                            ((55, 64), 0.00143),
                            ((65, 75), 0.00159),
                            ((76, 80), 0.00303)],  # avg 0.000769
        "Colorectal Cancer": [((0, 10), 0.0),
                              ((11, 17), 0.00021),
                              ((18, 25), 0.00021),
                              ((25, 34), 0.00229),
                              ((35, 44), 0.04572),
                              ((45, 59), 0.09144),
                              ((45, 54), 0.09144),
                              ((55, 64), 0.20574),
                              ((65, 75), 0.2286),
                              ((76, 80), 0.43435)],  # avg 0.11
        "Kidney (Renal) Cancer": [((0, 10), 0.0000005),
                                  ((11, 17), 0.00033),
                                  ((18, 25), 0.00333),
                                  ((25, 34), 0.0037),
                                  ((35, 44), 0.0074),
                                  ((45, 59), 0.01479),
                                  ((45, 54), 0.01849),
                                  ((55, 64), 0.03329),
                                  ((65, 75), 0.03698),
                                  ((76, 80), 0.07027)],  # AVG 0.01886
        "Leukemia": [((0, 10), 0.00017),
                     ((11, 17), 0.0003),
                     ((18, 25), 0.00301),
                     ((25, 34), 0.00334),
                     ((35, 44), 0.00668),
                     ((45, 59), 0.01002),
                     ((45, 54), 0.01336),
                     ((55, 64), 0.02004),
                     ((65, 75), 0.03341),
                     ((76, 80), 0.06347)],  # avg 0.01538
        "Liver Cancer": [((0, 10), 0.0),
                         ((11, 17), 0.0),
                         ((18, 25), 0.0000001),
                         ((25, 34), 0.000005),
                         ((35, 44), 0.0002),
                         ((45, 59), 0.00068),
                         ((45, 54), 0.0009),
                         ((55, 64), 0.00135),
                         ((65, 75), 0.00226),
                         ((76, 80), 0.00429)],  # AVG 0.000971
        "Lung Cancer": [((0, 10), 0.0),
                        ((11, 17), 0.00000001),
                        ((18, 25), 0.000001),
                        ((25, 34), 0.000008),
                        ((35, 44), 0.00609),
                        ((45, 59), 0.01739),
                        ((45, 54), 0.06086),
                        ((55, 64), 0.08694),
                        ((65, 75), 0.1478),
                        ((76, 80), 0.26083)],  # AVG 0.588
        "Melanoma of Skin": [((0, 10), 1e-05),
                             ((11, 17), 3e-05),
                             ((18, 25), 4e-05),
                             ((25, 34), 0.0002),
                             ((35, 44), 0.00563),
                             ((45, 59), 0.04826),
                             ((45, 54), 0.0563),
                             ((55, 64), 0.07238),
                             ((65, 75), 0.09651),
                             ((76,), 0.12064)],  # AVG 0.04
        "Non-Hodgkin Lymphoma": [((0, 10), 0.000001),
                                 ((11, 17), 0.000005),
                                 ((18, 25), 0.000003),
                                 ((25, 34), 0.00015),
                                 ((35, 44), 0.00429),
                                 ((45, 59), 0.02449),
                                 ((45, 54), 0.03062),
                                 ((55, 64), 0.04286),
                                 ((65, 75), 0.04899),
                                 ((76,), 0.06124)],  # AVG 0.02127
        "Ovarian Cancer": [((0, 10), 0.0),
                           ((11, 17), 0.000001),
                           ((18, 25), 0.000002),
                           ((25, 34), 0.000008),
                           ((35, 44), 0.00219),
                           ((45, 59), 0.00313),
                           ((45, 54), 0.00938),
                           ((55, 64), 0.0219),
                           ((65, 75), 0.02502),
                           ((76,), 0.05317)],  # AVG 0.1149
        "Pancreatic Cancer": [((0, 10), 0.0),
                              ((11, 17), 0.000004),
                              ((18, 25), 0.000005),
                              ((25, 34), 0.00023),
                              ((35, 44), 0.00631),
                              ((45, 59), 0.00902),
                              ((45, 54), 0.02706),
                              ((55, 64), 0.02706),
                              ((65, 75), 0.03608),
                              ((76,), 0.06315)],  # AVG 0.0169
        "Prostate Cancer": [((0, 10), 0.0),
                            ((11, 17), 0.0003),
                            ((18, 25), 0.00037),
                            ((25, 34), 0.00186),
                            ((35, 44), 0.01862),
                            ((45, 59), 0.03724),
                            ((45, 54), 0.14895),
                            ((55, 64), 0.22343),
                            ((65, 75), 0.2979),
                            ((76,), 0.52133)],  # AVG 0.125
        "Stomach (Gastric) Cancer": [((0, 10), 0.0),
                                     ((11, 17), 0.000001),
                                     ((18, 25), 0.000001),
                                     ((25, 34), 0.00016),
                                     ((35, 44), 0.0002),
                                     ((45, 59), 0.00023),
                                     ((45, 54), 0.00047),
                                     ((55, 64), 0.0014),
                                     ((65, 75), 0.00218),
                                     ((76, 80), 0.00296)],  # AVG 0.0007634
        "Testicular Cancer": [((0, 10), 0.0),
                              ((11, 17), 0.000005),
                              ((18, 25), 0.000005),
                              ((25, 34), 0.000007),
                              ((35, 44), 0.000008),
                              ((45, 59), 0.000049),
                              ((45, 54), 0.00049),
                              ((55, 64), 0.0007),
                              ((65, 75), 0.00099),
                              ((76, 80), 0.00211)],  # AVG 0.0004545
        "Thyroid Cancer": [((0, 10), 0.0),
                           ((11, 17), 0.0),
                           ((18, 25), 0.000001),
                           ((25, 34), 0.000006),
                           ((35, 44), 0.000007),
                           ((45, 59), 0.000008),
                           ((45, 54), 0.0004),
                           ((55, 64), 0.00057),
                           ((65, 75), 0.0008),
                           ((76, 80), 0.00172)]  # AVG 0.00037
    },
    SubAdmissionTypes.CARDIOLOGY.name: {
        "Aneurysms": [((0, 10), 0.0),
                      ((11, 17), 0.00037),
                      ((18, 25), 0.00042),
                      ((25, 34), 0.00465),
                      ((35, 44), 0.00535),
                      ((45, 59), 0.00553),
                      ((45, 54), 0.03255),
                      ((55, 64), 0.0465),
                      ((65, 75), 0.06511),
                      ((76, 80), 0.13951)],  # AVG 0.03
        "Arrhythmias": [((0, 10), 0.0),
                        ((11, 17), 0.00068),
                        ((18, 25), 0.00077),
                        ((25, 34), 0.00853),
                        ((35, 44), 0.0098),
                        ((45, 59), 0.01015),
                        ((45, 54), 0.05968),
                        ((55, 64), 0.08526),
                        ((65, 75), 0.11936),
                        ((76, 80), 0.25577)],  # AVG 0.055
        "Coronary Artery Disease": [((0, 10), 0.0),
                                    ((11, 17), 0.0),
                                    ((18, 25), 0.00039),
                                    ((25, 34), 0.00777),
                                    ((35, 44), 0.00893),
                                    ((45, 59), 0.00924),
                                    ((45, 54), 0.05436),
                                    ((55, 64), 0.07765),
                                    ((65, 75), 0.10871),
                                    ((76, 80), 0.23296)],  # AVG 0.05
        "Heart Attack": [((0, 10), 0.0),
                         ((11, 17), 0.0),
                         ((18, 25), 0.00013),
                         ((25, 34), 0.00133),
                         ((35, 44), 0.00666),
                         ((45, 59), 0.07987),
                         ((45, 54), 0.09318),
                         ((55, 64), 0.13312),
                         ((65, 75), 0.18636),
                         ((76, 80), 0.39935)],  # AVG 0.09
        "Heart Failure": [((0, 10), 0.0),
                          ((11, 17), 0.0),
                          ((18, 25), 0.00015),
                          ((25, 34), 0.00148),
                          ((35, 44), 0.0074),
                          ((45, 59), 0.08874),
                          ((45, 54), 0.10353),
                          ((55, 64), 0.14791),
                          ((65, 75), 0.20707),
                          ((76, 80), 0.44372)],  # AVG 0.1
        "Hypertension (High Blood Pressure)": [
            ((0, 10), 0.0229),
            ((11, 17), 0.0687),
            ((18, 25), 0.1145),
            ((25, 34), 0.22901),
            ((35, 44), 0.45802),
            ((45, 59), 0.61832),
            ((45, 54), 0.64122),
            ((55, 64), 0.72137),
            ((65, 75), 0.77863),
            ((76, 80), 0.84733)],  # AVG 0.45
        "Peripheral Artery Disease": [((0, 10), 0.0),
                                      ((11, 17), 0.0),
                                      ((18, 25), 0.0),
                                      ((25, 34), 0.0),
                                      ((35, 44), 0.01311),
                                      ((45, 59), 0.05246),
                                      ((45, 54), 0.10492),
                                      ((55, 64), 0.15738),
                                      ((65, 75), 0.20984),
                                      ((76, 80), 0.2623)],  # AVG 0.08
        "Stroke": [((0, 10), 0.0),
                   ((11, 17), 0.0),
                   ((18, 25), 0.0),
                   ((25, 34), 0.0),
                   ((35, 44), 0.00918),
                   ((45, 59), 0.03672),
                   ((45, 54), 0.07344),
                   ((55, 64), 0.11016),
                   ((65, 75), 0.14689),
                   ((76, 80), 0.18361)],  # AVG 0.056
        "Venous Thromboembolism": [((0, 10), 0.00036),
                               ((11, 17), 0.00073),
                               ((18, 25), 0.00109),
                               ((25, 34), 0.00145),
                               ((35, 44), 0.00182),
                               ((45, 59), 0.00218),
                               ((45, 54), 0.00255),
                               ((55, 64), 0.00291),
                               ((65, 75), 0.00327),
                               ((76, 80), 0.00364)]  # AVG 0.002
    },
    SubAdmissionTypes.DERMATOLOGY.name: {
        "Acne": {"male": [((0, 10), 0.0),
                          ((11, 17), 0.09998),
                          ((18, 25), 0.07142),
                          ((25, 34), 0.02857),
                          ((35, 44), 3e-05),
                          ((45, 59), 0.0),
                          ((45, 54), 0.0),
                          ((55, 64), 0.0),
                          ((65, 75), 0.0),
                          ((76, 80), 0.0)],  # 0.02 male
                 "female": [((0, 10), 0.0),
                            ((11, 17), 0.09132),
                            ((18, 25), 0.06523),
                            ((25, 34), 0.02609),
                            ((35, 44), 0.00027),
                            ((45, 59), 0.00652),
                            ((45, 54), 0.01044),
                            ((55, 64), 0.00013),
                            ((65, 75), 0.0),
                            ((76, 80), 0.0)]},  # 0.02 female
        "Cellulitis": [((0, 10), 0.0),
                       ((11, 17), 0.00042),
                       ((18, 25), 0.0003),
                       ((25, 34), 0.0012),
                       ((35, 44), 0.00246),
                       ((45, 59), 0.0042),
                       ((45, 54), 0.0054),
                       ((55, 64), 0.006),
                       ((65, 75), 0.012),
                       ((76, 80), 0.01801)],  # 0.05
        "Dermatitis": [((0, 10), 0.08521),
                       ((11, 17), 0.14912),
                       ((18, 25), 0.17042),
                       ((25, 34), 0.12781),
                       ((35, 44), 0.06391),
                       ((45, 59), 0.02982),
                       ((45, 54), 0.03834),
                       ((55, 64), 0.0213),
                       ((65, 75), 0.00852),
                       ((76, 80), 0.00554)],  # 0.07
        "Eczema": [((0, 10), 0.22135),
                   ((11, 17), 0.17708),
                   ((18, 25), 0.16822),
                   ((25, 34), 0.15937),
                   ((35, 44), 0.0664),
                   ((45, 59), 0.03099),
                   ((45, 54), 0.03984),
                   ((55, 64), 0.02213),
                   ((65, 75), 0.00885),
                   ((76, 80), 0.00576)],  # 0.09
        "Hives (Urticaria)": [((0, 10), 0.43229),
                              ((11, 17), 0.37486),
                              ((18, 25), 0.18836),
                              ((25, 34), 0.07411),
                              ((35, 44), 0.0315),
                              ((45, 59), 0.04323),
                              ((45, 54), 0.05558),
                              ((55, 64), 6e-05),
                              ((65, 75), 1e-05),
                              ((76, 80), 0.0)],  # 0.12
        "Impetigo": [((0, 10), 0.85224),
                     ((11, 17), 0.73901),
                     ((18, 25), 0.37133),
                     ((25, 34), 0.02435),
                     ((35, 44), 0.00122),
                     ((45, 59), 0.00085),
                     ((45, 54), 0.01096),
                     ((55, 64), 1e-05),
                     ((65, 75), 2e-05),
                     ((76, 80), 0.0)],  # 0.2
        "Psoriasis": [((0, 10), 0.00012),
                      ((11, 17), 0.00829),
                      ((18, 25), 0.05332),
                      ((25, 34), 0.06162),
                      ((35, 44), 0.03567),
                      ((45, 59), 0.01193),
                      ((45, 54), 0.03436),
                      ((55, 64), 0.05914),
                      ((65, 75), 0.0237),
                      ((76, 80), 0.01185)],  # 0.03
        "Rosacea": [((0, 10), 5e-05),
                    ((11, 17), 0.00033),
                    ((18, 25), 0.06987),
                    ((25, 34), 0.10247),
                    ((35, 44), 0.27993),
                    ((45, 59), 0.32637),
                    ((45, 54), 0.13508),
                    ((55, 64), 0.09274),
                    ((65, 75), 0.04659),
                    ((76, 80), 0.04658)],  # 0.11
        "Shingles (Herpes Zoster)": [((0, 10), 0.0),
                                     ((11, 17), 0.0),
                                     ((18, 25), 0.0),
                                     ((25, 34), 0.00062),
                                     ((35, 44), 0.01121),
                                     ((45, 59), 0.23659),
                                     ((45, 54), 0.48564),
                                     ((55, 64), 0.72223),
                                     ((65, 75), 0.75959),
                                     ((76, 80), 0.88411)],  # .31
    },
    SubAdmissionTypes.ENDOCRINOLOGY.name: {
        "Addison's Disease": [],
        "Cushing's Syndrome": [],
        "Diabetes - Type 1": [],
        "Diabetes - Type 2": [],
        "Gout": [],
        "Hyperlipidaemia": [],
        "Metabolic Syndrome": [],
        "Osteoporosis": [],
        "Pituitary Disorders": [],
        "Polycystic Ovary Syndrome (PCOS)": [],
        "Thyroid Disorders - including Hypothyroidism and Hyperthyroidism": []
    },
    SubAdmissionTypes.GASTROENTEROLOGY.name: {
        "Chronic Liver Disease - including Hepatitis and Cirrhosis": [],
        "Coeliac Disease": [],
        "Diverticular Disease": [],
        "Gallstones": [],
        "Gastro-oesophageal Reflux Disease (GORD)": [],
        "Gastroenteritis": [],
        "Inflammatory Bowel Disease (IBD) - including Crohn's Disease and Ulcerative Colitis": [],
        "Irritable Bowel Syndrome (IBS)": [],
        "Pancreatitis": [],
        "Peptic Ulcers": []},
    SubAdmissionTypes.GASTROINTESTINAL_DISORDERS.name: {
        "Celiac Disease": [],
        "Cirrhosis": [],
        "Crohn's Disease": [],
        "Gallstones": [],
        "Gastroesophageal Reflux Disease (GERD)": [],
        "Hepatitis": [],
        "Irritable Bowel Syndrome (IBS)": [],
        "Pancreatitis": [],
        "Peptic Ulcer Disease": [],
        "Ulcerative Colitis": []},
    SubAdmissionTypes.GERIATRICS.name: {

    },
    SubAdmissionTypes.HEMATOLOGY.name: {
        "Anemia": [],
        "Deep Vein Thrombosis (DVT)": [],
        "Hemochromatosis": [],
        "Hemophilia": [],
        "Iron Deficiency Anemia": [],
        "Leukemia": [],
        "Lymphoma": [],
        "Polycythemia Vera": [],
        "Sickle Cell Disease": [],
        "Thrombocytopenia": []},
    SubAdmissionTypes.INFECTIOUS_DISEASES.name: {
        "COVID-19": [],
        "HIV/AIDS": [],
        "Hepatitis": [],
        "Herpes Simplex Virus": [],
        "Influenza": [],
        "Malaria": [],
        "Strep Throat": [],
        "Tuberculosis": [],
        "Urinary Tract Infections (UTIs)": []},
    SubAdmissionTypes.INJURY_RTC.name: {
        "Abrasions": [],
        "Acoustic Trauma": [],
        "Airbag Injuries": [],
        "Amputations": [],
        "Burn Injuries": [],
        "Bursitis": [],
        "Cervical Spine Injuries": [],
        "Compartment Syndrome": [],
        "Concussions": [],
        "Contusions (bruises)": [],
        "Crush Injuries": [],
        "Dental Injuries": [],
        "Dislocations": [],
        "Drowning or Near-Drowning Incidents": [],
        "Eye Injuries": [],
        "Facial Fractures": [],
        "Fractures": [],
        "Heatstroke": [],
        "Hematomas": [],
        "Hypothermia or Frostbite": [],
        "Internal Bleeding": [],
        "Lacerations": [],
        "Lower Extremity Injuries": [],
        "Lumbar Spine Injuries": [],
        "Nerve Damage": [],
        "Organ Damage": [],
        "Pelvic Fractures": [],
        "Pneumothorax (collapsed lung)": [],
        "Post-Traumatic Arthritis": [],
        "Psychological Trauma": [],
        "Rib Fractures": [],
        "Seat Belt Injuries": [],
        "Skull Fractures": [],
        "Soft Tissue Injuries": [],
        "Spinal Cord Injuries": [],
        "Sprains": [],
        "Strains": [],
        "Stress Fractures": [],
        "Tendon Injuries": [],
        "Thoracic Spine Injuries": [],
        "Traumatic Brain Injuries (TBIs)": [],
        "Upper Extremity Injuries": [],
        "Whiplash": []},
    SubAdmissionTypes.MATERNITY.name: {
        "Antepartum Haemorrhage": [],
        "Gestational Diabetes Monitoring": [],
        "Induction of Labour": [],
        "Labour and Delivery": [],
        "Postpartum Complications": [],
        "Pre-eclampsia/Eclampsia": [],
        "Pregnancy-induced Hypertension": [],
        "Preterm Labour": [],
        "Ruptured Membranes without Contractions": [],
        "Scheduled Caesarean Section": []},
    SubAdmissionTypes.MUSCULOSKELETAL.name: {
        "Ankylosing Spondylitis": [],
        "Bursitis": [],
        "Fibromyalgia": [],
        "Gout": [],
        "Low Back Pain": [],
        "Lupus": [],
        "Plantar Fasciitis": [],
        "Polymyalgia Rheumatica": [],
        "Repetitive Strain Injury (RSI)": [],
        "Tendinitis": []},
    SubAdmissionTypes.NEPHROLOGY.name: {
        "Acute Kidney Injury (AKI)": [],
        "Chronic Kidney Disease (CKD)": [],
        "Glomerulonephritis": [],
        "Haemodialysis-related Amyloidosis": [],
        "Hyperkalaemia": [],
        "Nephrotic Syndrome": [],
        "Renal Artery Stenosis": [],
        "Polycystic Kidney Disease": [],
        "Kidney Stones": [],
        "Urinary Tract Infections (UTIs)": [],
    },
    SubAdmissionTypes.NEUROLOGY.name: {
        "Alzheimer's Disease": [],
        "Bell's Palsy": [],
        "Concussion": [],
        "Epilepsy": [],
        "Migraines": [],
        "Multiple Sclerosis": [],
        "Parkinson's Disease": [],
        "Peripheral Neuropathy": [],
        "Sciatica": [],
        "Stroke": []
    },
    SubAdmissionTypes.OBSTETRICS.name: {
        "Breast Disorders": [],
        "Congenital Reproductive Anomalies": [],
        "Endometriosis": [],
        "Gynecological Tumors": [],
        "Menstrual Disorders": [],
        "Polycystic Ovary Syndrome (PCOS)": [],
        "Precocious Puberty": [],
        "Premature Ovarian Insufficiency (POI)": [],
        "Turner Syndrome": [],
        "Vulvovaginitis": []
    },
    SubAdmissionTypes.ONCOLOGY.name: {
        "Bladder Cancer": [],
        "Breast Cancer": [],
        "Colorectal Cancer": [],
        "Leukemia": [],
        "Lung Cancer": [],
        "Lymphoma": [],
        "Melanoma": [],
        "Ovarian Cancer": [],
        "Pancreatic Cancer": [],
        "Prostate Cancer": []
    },
    SubAdmissionTypes.OPHTHALMOLOGY.name: {
        "Age-related Macular Degeneration (AMD)": [],
        "Cataracts": [],
        "Conjunctivitis": [],
        "Diabetic Retinopathy": [],
        "Dry Eye Syndrome": [],
        "Glaucoma": [],
        "Keratitis": [],
        "Refractive Errors": [],
        "Retinal Detachment": [],
        "Uveitis": []
    },
    SubAdmissionTypes.ORTHOPEDICS.name: {
        "Anterior Cruciate Ligament (ACL) Injuries": [],
        "Carpal Tunnel Syndrome": [],
        "Fractures": [],
        "Meniscus Tears": [],
        "Osteoarthritis": [],
        "Osteoporosis": [],
        "Rheumatoid Arthritis": [],
        "Rotator Cuff Tears": [],
        "Scoliosis": [],
        "Spinal Disc Herniation": []
    },
    SubAdmissionTypes.OTORHINOLARYNGOLOGY_ENT.name: {
        "Hearing Loss": [],
        "Laryngitis": [],
        "Meniere's Disease": [],
        "Otitis Externa (Swimmer's Ear)": [],
        "Otitis Media (Middle Ear Infection)": [],
        "Pharyngitis": [],
        "Rhinitis": [],
        "Sinusitis": [],
        "Tinnitus": [],
        "Tonsillitis": []
    },
    SubAdmissionTypes.PSYCHIATRIC.name: {
        "Anxiety Disorders": [],
        "Attention Deficit Hyperactivity Disorder (ADHD)": [],
        "Autism Spectrum Disorder": [],
        "Bipolar Disorder": [],
        "Depression": [],
        "Eating Disorders (Anorexia, Bulimia)": [],
        "Insomnia": [],
        "Obsessive-Compulsive Disorder (OCD)": [],
        "Post-Traumatic Stress Disorder (PTSD)": [],
        "Schizophrenia": []
    },
    SubAdmissionTypes.RESPIRATORY.name: {
        "Allergic Rhinitis": [],
        "Asthma": [],
        "Bronchitis": [],
        "Chronic Obstructive Pulmonary Disease (COPD)": [],
        "Cystic Fibrosis": [],
        "Lung Cancer": [],
        "Pneumonia": [],
        "Pulmonary Embolism": [],
        "Sinusitis": [],
        "Sleep Apnea": []
    },
    SubAdmissionTypes.SELF_INFLICTED.name: {
        "Bone breaking": [],
        "Burning": [],
        "Hair pulling (Trichotillomania)": [],
        "Head banging": [],
        "Ingesting harmful substances": [],
        "Lacerations or cuts": [],
        "Overdose": [],
        "Piercing the skin": [],
        "Self-hitting": [],
        "Skin picking (Dermatillomania)": []}
}
