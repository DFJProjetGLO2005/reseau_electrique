from requetes import Requetes
from listeBris import ListeBris
from listeCentrales import ListeCentrales
from listeVilles import ListeVilles
from listeEquipements import ListeEquipements
from listeAbonnes import ListeAbonnes
from listeConsommationsMensuelles import ListeConsommationsMensuelles





if __name__ == "__main__":
    req = Requetes('root', 'tetuda')
    test = {'eid': 'SUPP24046',
    'date': "2016-05-09 23:02:52",
    'nom': 'Support: PYLONE HAUBANE A CHAINETTE',
    'ville': 'Durham-Sud',
    'nb_abonnes': 121, 'aids': [2981, 2982, 2983, 2984, 2985, 2986, 2987, 2988, 2989, 2990, 2991, 2992, 2993, 2994, 2995, 2996, 2997, 2998, 2999, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3041, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050, 3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3061, 3062, 3063, 3064, 3065, 3066, 3067, 3068, 3069, 3070, 3071, 3072, 3073, 3074, 3075, 3076, 3077, 3078, 3079, 3080, 3081, 3082, 3083, 3084, 3085, 3086, 3087, 3088, 3089, 3090, 3091, 3092, 3093, 3094, 3095, 3096, 3097, 3098, 3099, 3100, 3101],
    'raccordements': ['RACC02981', 'RACC02982', 'RACC02983', 'RACC02984', 'RACC02985', 'RACC02986', 'RACC02987', 'RACC02988', 'RACC02989', 'RACC02990', 'RACC02991', 'RACC02992', 'RACC02993', 'RACC02994', 'RACC02995', 'RACC02996', 'RACC02997', 'RACC02998', 'RACC02999', 'RACC03000', 'RACC03001', 'RACC03002', 'RACC03003', 'RACC03004', 'RACC03005', 'RACC03006', 'RACC03007', 'RACC03008', 'RACC03009', 'RACC03010', 'RACC03011', 'RACC03012', 'RACC03013', 'RACC03014', 'RACC03015', 'RACC03016', 'RACC03017', 'RACC03018', 'RACC03019', 'RACC03020', 'RACC03021', 'RACC03022', 'RACC03023', 'RACC03024', 'RACC03025', 'RACC03026', 'RACC03027', 'RACC03028', 'RACC03029', 'RACC03030', 'RACC03031', 'RACC03032', 'RACC03033', 'RACC03034', 'RACC03035', 'RACC03036', 'RACC03037', 'RACC03038', 'RACC03039', 'RACC03040', 'RACC03041', 'RACC03042', 'RACC03043', 'RACC03044', 'RACC03045', 'RACC03046', 'RACC03047', 'RACC03048', 'RACC03049', 'RACC03050', 'RACC03051', 'RACC03052', 'RACC03053', 'RACC03054', 'RACC03055', 'RACC03056', 'RACC03057', 'RACC03058', 'RACC03059', 'RACC03060', 'RACC03061', 'RACC03062', 'RACC03063', 'RACC03064', 'RACC03065', 'RACC03066', 'RACC03067', 'RACC03068', 'RACC03069', 'RACC03070', 'RACC03071', 'RACC03072', 'RACC03073', 'RACC03074', 'RACC03075', 'RACC03076', 'RACC03077', 'RACC03078', 'RACC03079', 'RACC03080', 'RACC03081', 'RACC03082', 'RACC03083', 'RACC03084', 'RACC03085', 'RACC03086', 'RACC03087', 'RACC03088', 'RACC03089', 'RACC03090', 'RACC03091', 'RACC03092', 'RACC03093', 'RACC03094', 'RACC03095', 'RACC03096', 'RACC03097', 'RACC03098', 'RACC03099', 'RACC03100', 'RACC03101'],
    'estimation_conso': 736281.25}
    bris = {'eid': 'SUPP01981', 'date': '2016-12-13 02:43:02', 'nom': 'Support: PYLONE A TREILLIS', 'ville': 'Stornoway', 'nb_abonnes': 1, 'aids': [268], 'raccordements': ['RACC00268'], 'estimation_conso': 2691.5}
    #z = ListeBris(req).get_data("estimation_conso")
    #z = ListeBris(req).get_liste_Details(test['eid'], test['date'], test['nom'], test['ville'], test['nb_abonnes'], test['aids'], test['raccordements'], test['estimation_conso'])
    #ListeBris(req).resoudre_bris(bris['eid'], bris['date'])
    z = ListeVilles(req).get_data()
    #z = ListeCentrales(req).get_data()
    #z = ListeEquipements(req).get_data("Durham-Sud")
    #z = ListeAbonnes(req).get_data(test["aids"])
    #z = ListeConsommationsMensuelles(req).get_data(123)
    print(z)
    #for i in z:
    #    print(i)
