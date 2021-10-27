def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/61796fade4279b249c0098f5

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] 
        Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository[*]. Irvine, CA: University of California, School of Information and Computer Science.
        
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI Machine Learning Repository: http://archive.ics.uci.edu/ml
    """
    if (glucose is None):
        return u'False'
    if (glucose > 154):
        if (bmi is None):
            return u'True'
        if (bmi > 29.34583):
            if (insulin is None):
                return u'True'
            if (insulin > 249):
                if (bmi > 44.9):
                    return u'False'
                if (bmi <= 44.9):
                    if (glucose > 163):
                        if (diabetes_pedigree is None):
                            return u'True'
                        if (diabetes_pedigree > 2.233):
                            return u'False'
                        if (diabetes_pedigree <= 2.233):
                            return u'True'
                    if (glucose <= 163):
                        if (blood_pressure is None):
                            return u'False'
                        if (blood_pressure > 72):
                            return u'False'
                        if (blood_pressure <= 72):
                            if (bmi > 33.35):
                                return u'True'
                            if (bmi <= 33.35):
                                return u'False'
            if (insulin <= 249):
                if (skinfold is None):
                    return u'True'
                if (skinfold > 31):
                    return u'True'
                if (skinfold <= 31):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 1.407):
                        return u'False'
                    if (diabetes_pedigree <= 1.407):
                        if (bmi > 34.25):
                            return u'True'
                        if (bmi <= 34.25):
                            if (bmi > 33.45):
                                if (blood_pressure is None):
                                    return u'False'
                                if (blood_pressure > 66):
                                    return u'False'
                                if (blood_pressure <= 66):
                                    if (skinfold > 27):
                                        return u'True'
                                    if (skinfold <= 27):
                                        return u'False'
                            if (bmi <= 33.45):
                                if (diabetes_pedigree > 0.3005):
                                    return u'True'
                                if (diabetes_pedigree <= 0.3005):
                                    if (bmi > 29.85):
                                        if (diabetes_pedigree > 0.2835):
                                            return u'False'
                                        if (diabetes_pedigree <= 0.2835):
                                            return u'True'
                                    if (bmi <= 29.85):
                                        return u'False'
        if (bmi <= 29.34583):
            if (blood_pressure is None):
                return u'False'
            if (blood_pressure > 79):
                return u'False'
            if (blood_pressure <= 79):
                if (pregnancies is None):
                    return u'True'
                if (pregnancies > 1):
                    if (bmi > 26.25):
                        if (skinfold is None):
                            return u'False'
                        if (skinfold > 8):
                            return u'True'
                        if (skinfold <= 8):
                            return u'False'
                    if (bmi <= 26.25):
                        return u'True'
                if (pregnancies <= 1):
                    return u'False'
    if (glucose <= 154):
        if (glucose > 103):
            if (age is None):
                return u'False'
            if (age > 30):
                if (bmi is None):
                    return u'False'
                if (bmi > 26.4381):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 0.313):
                        if (bmi > 42.9375):
                            return u'True'
                        if (bmi <= 42.9375):
                            if (age > 42):
                                if (age > 53):
                                    if (diabetes_pedigree > 0.5425):
                                        if (skinfold is None):
                                            return u'False'
                                        if (skinfold > 27):
                                            if (bmi > 32):
                                                return u'True'
                                            if (bmi <= 32):
                                                return u'False'
                                        if (skinfold <= 27):
                                            return u'False'
                                    if (diabetes_pedigree <= 0.5425):
                                        return u'True'
                                if (age <= 53):
                                    if (bmi > 27.9):
                                        return u'True'
                                    if (bmi <= 27.9):
                                        if (diabetes_pedigree > 0.5385):
                                            return u'True'
                                        if (diabetes_pedigree <= 0.5385):
                                            return u'False'
                            if (age <= 42):
                                if (insulin is None):
                                    return u'True'
                                if (insulin > 220):
                                    return u'False'
                                if (insulin <= 220):
                                    if (glucose > 152):
                                        return u'False'
                                    if (glucose <= 152):
                                        if (glucose > 141):
                                            return u'True'
                                        if (glucose <= 141):
                                            if (glucose > 132):
                                                return u'False'
                                            if (glucose <= 132):
                                                if (blood_pressure is None):
                                                    return u'True'
                                                if (blood_pressure > 81):
                                                    return u'True'
                                                if (blood_pressure <= 81):
                                                    if (blood_pressure > 79):
                                                        return u'False'
                                                    if (blood_pressure <= 79):
                                                        if (bmi > 33.2):
                                                            return u'True'
                                                        if (bmi <= 33.2):
                                                            if (blood_pressure > 71):
                                                                return u'True'
                                                            if (blood_pressure <= 71):
                                                                if (diabetes_pedigree > 0.7205):
                                                                    if (pregnancies is None):
                                                                        return u'True'
                                                                    if (pregnancies > 4):
                                                                        return u'True'
                                                                    if (pregnancies <= 4):
                                                                        return u'False'
                                                                if (diabetes_pedigree <= 0.7205):
                                                                    return u'False'
                    if (diabetes_pedigree <= 0.313):
                        if (bmi > 28.05):
                            if (diabetes_pedigree > 0.26125):
                                if (bmi > 35.2):
                                    return u'False'
                                if (bmi <= 35.2):
                                    if (blood_pressure is None):
                                        return u'False'
                                    if (blood_pressure > 85):
                                        return u'False'
                                    if (blood_pressure <= 85):
                                        if (bmi > 30.95):
                                            return u'True'
                                        if (bmi <= 30.95):
                                            return u'False'
                            if (diabetes_pedigree <= 0.26125):
                                if (insulin is None):
                                    return u'True'
                                if (insulin > 143):
                                    return u'True'
                                if (insulin <= 143):
                                    if (diabetes_pedigree > 0.219):
                                        if (pregnancies is None):
                                            return u'True'
                                        if (pregnancies > 11):
                                            return u'False'
                                        if (pregnancies <= 11):
                                            if (skinfold is None):
                                                return u'True'
                                            if (skinfold > 39):
                                                return u'False'
                                            if (skinfold <= 39):
                                                if (pregnancies > 9):
                                                    if (bmi > 29.75):
                                                        return u'False'
                                                    if (bmi <= 29.75):
                                                        return u'True'
                                                if (pregnancies <= 9):
                                                    return u'True'
                                    if (diabetes_pedigree <= 0.219):
                                        if (pregnancies is None):
                                            return u'False'
                                        if (pregnancies > 5):
                                            if (glucose > 115):
                                                if (bmi > 32.35):
                                                    return u'True'
                                                if (bmi <= 32.35):
                                                    if (bmi > 29.7):
                                                        return u'False'
                                                    if (bmi <= 29.7):
                                                        return u'True'
                                            if (glucose <= 115):
                                                return u'False'
                                        if (pregnancies <= 5):
                                            return u'False'
                        if (bmi <= 28.05):
                            return u'False'
                if (bmi <= 26.4381):
                    if (age > 59):
                        if (bmi > 24.4):
                            return u'False'
                        if (bmi <= 24.4):
                            return u'True'
                    if (age <= 59):
                        return u'False'
            if (age <= 30):
                if (pregnancies is None):
                    return u'False'
                if (pregnancies > 6):
                    return u'True'
                if (pregnancies <= 6):
                    if (diabetes_pedigree is None):
                        return u'False'
                    if (diabetes_pedigree > 0.30131):
                        if (skinfold is None):
                            return u'False'
                        if (skinfold > 32):
                            if (bmi is None):
                                return u'False'
                            if (bmi > 36):
                                if (bmi > 40.25):
                                    if (diabetes_pedigree > 0.373):
                                        if (diabetes_pedigree > 0.61):
                                            if (insulin is None):
                                                return u'False'
                                            if (insulin > 230):
                                                return u'False'
                                            if (insulin <= 230):
                                                return u'True'
                                        if (diabetes_pedigree <= 0.61):
                                            return u'False'
                                    if (diabetes_pedigree <= 0.373):
                                        return u'True'
                                if (bmi <= 40.25):
                                    return u'False'
                            if (bmi <= 36):
                                if (bmi > 33.25):
                                    return u'True'
                                if (bmi <= 33.25):
                                    if (insulin is None):
                                        return u'False'
                                    if (insulin > 132):
                                        return u'True'
                                    if (insulin <= 132):
                                        return u'False'
                        if (skinfold <= 32):
                            if (age > 29):
                                if (blood_pressure is None):
                                    return u'True'
                                if (blood_pressure > 71):
                                    return u'False'
                                if (blood_pressure <= 71):
                                    return u'True'
                            if (age <= 29):
                                if (skinfold > 5):
                                    if (diabetes_pedigree > 0.5385):
                                        if (pregnancies > 0):
                                            if (diabetes_pedigree > 0.685):
                                                return u'False'
                                            if (diabetes_pedigree <= 0.685):
                                                if (bmi is None):
                                                    return u'False'
                                                if (bmi > 25.8):
                                                    if (diabetes_pedigree > 0.57):
                                                        return u'False'
                                                    if (diabetes_pedigree <= 0.57):
                                                        return u'True'
                                                if (bmi <= 25.8):
                                                    return u'True'
                                        if (pregnancies <= 0):
                                            if (blood_pressure is None):
                                                return u'True'
                                            if (blood_pressure > 74):
                                                return u'False'
                                            if (blood_pressure <= 74):
                                                return u'True'
                                    if (diabetes_pedigree <= 0.5385):
                                        return u'False'
                                if (skinfold <= 5):
                                    if (glucose > 133):
                                        if (glucose > 144):
                                            if (bmi is None):
                                                return u'False'
                                            if (bmi > 33.9):
                                                return u'True'
                                            if (bmi <= 33.9):
                                                return u'False'
                                        if (glucose <= 144):
                                            return u'True'
                                    if (glucose <= 133):
                                        if (blood_pressure is None):
                                            return u'False'
                                        if (blood_pressure > 79):
                                            if (bmi is None):
                                                return u'True'
                                            if (bmi > 31.75):
                                                return u'True'
                                            if (bmi <= 31.75):
                                                return u'False'
                                        if (blood_pressure <= 79):
                                            return u'False'
                    if (diabetes_pedigree <= 0.30131):
                        if (glucose > 111):
                            if (blood_pressure is None):
                                return u'False'
                            if (blood_pressure > 78):
                                return u'False'
                            if (blood_pressure <= 78):
                                if (bmi is None):
                                    return u'False'
                                if (bmi > 26.35):
                                    if (skinfold is None):
                                        return u'False'
                                    if (skinfold > 9):
                                        if (bmi > 26.9):
                                            if (diabetes_pedigree > 0.2005):
                                                return u'False'
                                            if (diabetes_pedigree <= 0.2005):
                                                if (diabetes_pedigree > 0.186):
                                                    return u'True'
                                                if (diabetes_pedigree <= 0.186):
                                                    return u'False'
                                        if (bmi <= 26.9):
                                            return u'True'
                                    if (skinfold <= 9):
                                        return u'True'
                                if (bmi <= 26.35):
                                    return u'False'
                        if (glucose <= 111):
                            return u'False'
        if (glucose <= 103):
            if (bmi is None):
                return u'False'
            if (bmi > 27.13929):
                if (diabetes_pedigree is None):
                    return u'False'
                if (diabetes_pedigree > 0.65):
                    if (diabetes_pedigree > 0.6755):
                        if (pregnancies is None):
                            return u'False'
                        if (pregnancies > 2):
                            if (diabetes_pedigree > 0.796):
                                if (glucose > 94):
                                    if (bmi > 37.25):
                                        return u'True'
                                    if (bmi <= 37.25):
                                        return u'False'
                                if (glucose <= 94):
                                    return u'True'
                            if (diabetes_pedigree <= 0.796):
                                return u'False'
                        if (pregnancies <= 2):
                            return u'False'
                    if (diabetes_pedigree <= 0.6755):
                        return u'True'
                if (diabetes_pedigree <= 0.65):
                    if (bmi > 30.63333):
                        if (bmi > 31.03333):
                            if (glucose > 89):
                                if (blood_pressure is None):
                                    return u'False'
                                if (blood_pressure > 83):
                                    if (blood_pressure > 97):
                                        return u'False'
                                    if (blood_pressure <= 97):
                                        return u'True'
                                if (blood_pressure <= 83):
                                    if (insulin is None):
                                        return u'False'
                                    if (insulin > 35):
                                        return u'False'
                                    if (insulin <= 35):
                                        if (skinfold is None):
                                            return u'False'
                                        if (skinfold > 41):
                                            return u'True'
                                        if (skinfold <= 41):
                                            if (bmi > 35.65):
                                                return u'False'
                                            if (bmi <= 35.65):
                                                if (skinfold > 27):
                                                    return u'False'
                                                if (skinfold <= 27):
                                                    if (glucose > 94):
                                                        return u'True'
                                                    if (glucose <= 94):
                                                        return u'False'
                            if (glucose <= 89):
                                return u'False'
                        if (bmi <= 31.03333):
                            if (diabetes_pedigree > 0.4225):
                                return u'False'
                            if (diabetes_pedigree <= 0.4225):
                                return u'True'
                    if (bmi <= 30.63333):
                        return u'False'
            if (bmi <= 27.13929):
                return u'False'
