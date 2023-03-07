%procedure to allow adding to a list repeatedly
:-dynamic(omicronVariantUnderlyingConditionsSymptoms/1).
:-dynamic (stats/2).
:-dynamic (riskCountry/1).

stats(0,0).

% **********************Lists of symptoms by variants - Facts**************************************************

%delta variant Symptom
listOfVariantSymptoms([fever,chills,soreThroat,cough,lowEnergy,fatigue,headache,nausea,lossOfSmell,lossOfTaste,runnyNose,shortnessOfBreath,tiredness,muscleAche,chestPain,diarrhoea,irritatedEyes,blurredVision,lightSensitivity,dizziness,vomiting],deltaVariant).

%omicron variant Symptom
listOfVariantSymptoms([runnyNose,headache,fatigue,sneezing,soreThroat,cough,hoarseVoice,chills,shivers,fever,dizziness,brainFog,musclePains,lossOfSmell,chestPain,nightSweats,tiredness, diarrhoea],omicronVariant).

%no variant
listOfVariantSymptoms([_],noVariant).


%*********************Diagnoses for variants of Covid - Facts***************************************************

%regular covid symptom
listOfSymptoms([fever,cough,tiredness,runnyNose,soreThroat,headache,lossOfTaste,lossOfSmell,shortnessOfBreath,musclePain,jointPain,nausea,lossOfAppetite,diarrhoea,vomiting],regularCovidSymptoms).

%mild omicron symptom
listOfSymptoms([fever,dryCough,runnyNose,scratchySoreThroat,headache,nausea,lossOfAppetite,cold,congestion,sneezing,fatigue,hoarseVoice,chills,shiver,dizziness,brainFog],mildOmicronSymptoms).

%severe omicron symptom
listOfSymptoms([difficultyBreathing,shortnessOfBreath,lossOfSpeech,lossOfMobility,confusion,chestPain,hospitalization,death],severeOmicronSymptoms).

%mild delta symptom
listOfSymptoms([fever,runnyNose,soreThroat,headache,lossOfTaste,lossOfSmell,sneezing,lowEnergy,cold,fatigue],mildDeltaSymptoms).

%severe delta symptom
listOfSymptoms([difficultyBreathing,shortnessOfBreath,lossOfMobility,confusion,chestPain,hospitalization,death],severeDeltaSymptom).

%covid symptom
listOfSymptoms([fever,cough],covid).

%no covid
listOfSymptoms([_],covidFree).


% **********************Omicron Variant Underlying Conditions -Facts**************************************

%list of underlying conditions associated with Omicron Variant
omicronVariantUnderlyingConditionsSymptoms(['Cancer','Cerebrovascular disease','Chronic kidney disease','Interstitial lung disease','Pulmonary embolism','Pulmonary hypertension','Bronchiectasis','Cirrhosis','Non-alcoholic fatty liver disease','Alcoholic liver disease','Autoimmune hepatitis','Cystic fibrosis','Diabetes','ADHD','Cerebral Palsy','Congenital Malformations','Spinal Cord Injuries','heart failure','coronary artery disease','cardiomyopathies','HIV','Mood disorders','depression','Schizophrenia spectrum disorders','dementia','Obesity','Physical inactivity','Smoking','Tuberculosis','Overweight','Sickle cell disease','Substance use disorders','Thalassemia','Alpha 1 antitrypsin deficiency','Asthma','Bronchopulmonary dysplasia','Hepatitis B','Hepatitis C','Hypertension']).


%allowing the user to insert other contributory factors
update_omicronVariantUnderlyingConditionsSymptoms:-nl,write('New Condition: '),nl,read(Condition),
                     omicronVariantUnderlyingConditionsSymptoms(Oldlist),append(Oldlist,[Condition],Newlist),
                     retractall(omicronVariantUnderlyingConditionsSymptoms(_)),
                     assert(omicronVariantUnderlyingConditionsSymptoms(Newlist)),
                     omicronVariantUnderlyingConditionsSymptoms(X),
                     nl,write(X),
                     nl,write('Do you wish to add another? '),nl,read(Ans),
                     ((Ans=='y';Ans=='Y')->update_omicronVariantUnderlyingConditionsSymptoms;write('Goodbye')).



% *********************At Risk for having Covid - Facts***************************************************
/*
 * These are the risk factors for covid
 * If the "Risk is 4" then the person is at risk of having covid
 */

%people over 65
oldAge(Age,OldAgeval):- Age >= 65 -> OldAgeval is 1; OldAgeval is 0.

%people who do not wash their hands or wear masks
ignoresCovidProtocols(IgnoresProtocols,Ignoreval):- IgnoresProtocols == true -> Ignoreval is 1; Ignoreval is 0.

% people who come in contact with someone who has the virus within 14
% days
exposureToCovid(CovidExposure,Exposureval):- CovidExposure == true -> Exposureval is 1; Exposureval is 0.

%people with underlying medical conditions
underlyingMedicalConditions(UnderlyingConditions,Underlyingval):- UnderlyingConditions == true -> Underlyingval is 1; Underlyingval is 0.

%people who have been in poorly ventilated rooms with several persons
poorlyVentilatedCrowedRooms(PoorlyVentilated,Poorlyval):- PoorlyVentilated == true -> Poorlyval is 1; Poorlyval is 0.

%people who are overweight
excessivelyOverweight(ExcessiveWeight,Excessiveval):-ExcessiveWeight == true -> Excessiveval is 1; Excessiveval is 0.

%people who does not exercise
lackOfExercise(NoExercise,NoExerciseval):-NoExercise == true -> NoExerciseval is 1; NoExerciseval is 0.

%people who smokes a lot in the past or present
heavySmoker(Smoker,Smokerval):- Smoker == true -> Smokerval is 1; Smokerval is 0.

%the amount of symptoms a person should have - at least 4
lengthOfSymptoms(Count,SymptomRisk):- SymptomRisk is Count/3.

%the amount of underlying disease a person have
lengthOfUnderlyingDiseases(Count,UnderlyingRisk):- UnderlyingRisk is Count/3.


% *********************At Risk for having Covid -Rules***************************************************

findlength([],X):-X is 0.
findlength([_|Tail],Count):-findlength(Tail,Prev),Count is Prev + 1.


% ***********************************BLOOD PRESSURE CONSIDERATIONS****************************************

%calculating blood pressure value
bloodPressureCalculator(SystolicValue,DiastolicValue,BPValue):- (SystolicValue < 90; DiastolicValue < 60)-> BPValue is 4;
     BPValue is 0.

%blood pressure can be high or low
bloodPressure(low).
bloodPressure(high).


%Showing Statistics for people with high blood pressure
displayHighBloodPressureStats:- stats(TotalPersons,TotalHighBloodPressure),
    nl, write('The Total Persons is: '), write(TotalPersons),
    nl, write('The Total Persons with High Blood Pressure is: '), write(TotalHighBloodPressure),
    findPercentage(TotalHighBloodPressure,TotalPersons,Percent),
    nl, write('Percentage of persons with high blood pressure: '), write(Percent), write('%').


% **************************************CALCULATIONS ***************************************************

%converting celsius to fahrenheit
convertCelToFah(CelsiusTemp,FahrenheitTemp):- FahrenheitTemp is ((CelsiusTemp * 1.8) + 32).

%checking if fever is present using fahrenheit temperature
checkingForFever(FahrenheitTemp,Fever):- FahrenheitTemp >= 100.4 -> Fever is 1; Fever is 0.

%finding all percentages
findPercentage(Subset,Total,Percent):- Percent is ((Subset / Total) * 100 ).

%converting height from inches and feet to meters
heightInMeters(HeightFeet,HeightInches,HeightMeters):- HeightMeters is (HeightFeet * 0.3048)+(HeightInches * 0.0254).

%converting weight from pounds to kilogram
weightInKilo(WeightPounds,WeightKilo):- WeightKilo is (WeightPounds * 0.4536).

%calulating body mass index and assigns a value based on it
bmiCalculator(WeightKilo,HeightMeters,BMI,BMIValue):- BMI is WeightKilo/(HeightMeters * HeightMeters),
     (BMI =< 18.5 -> BMIValue is -1,
     nl, write('Underweight: Consult your doctor to see how you can improve your weight.'),
     nl, write('Eat more more frequently choosing nutrition rich foods.'); /*Underweight*/
     BMI >= 18.5, BMI =< 24.9 -> BMIValue is 0,
     nl, write('Normal Weight: Continue to maintain a healthy lifestyle'); /*Normal Weight*/
     BMI >= 25.0, BMI =< 29.9 -> BMIValue is 1,
     nl, write('Overweight: Consume plenty of fruits and vegetables and limit excess calories, fat and sugar.'),/*overweight*/
     BMI >= 30.0 -> BMIValue is 2),
     nl, write('Obese: Eat a balanced diet.'). /*Obese*/


totalRisk(Age,Protocols, Exposure, UnderlyingConditions, PoorlyVentilated, ExcessiveWeight, Exercise, Smoker, SymptomsCount, UnderlyingDiseasesCount, TotalRisk, Diag):- oldAge(Age,A),
     ignoresCovidProtocols(Protocols, B),
     exposureToCovid(Exposure,C),
     underlyingMedicalConditions(UnderlyingConditions,D),
     poorlyVentilatedCrowedRooms(PoorlyVentilated,E),
     excessivelyOverweight(ExcessiveWeight,F),
     lackOfExercise(Exercise,G),
     heavySmoker(Smoker,H),
     lengthOfSymptoms(SymptomsCount,I),
     lengthOfUnderlyingDiseases(UnderlyingDiseasesCount,J),
     TotalRisk is A+B+C+D+E+F+G+H+I+J, write('Risk Level'), nl, write(TotalRisk),
     diagnoses(TotalRisk,Diag), nl, write(Diag).

diagnoses(TotalRisk, Diag):-
     TotalRisk >= 5 -> Diag = "You are at high risk of having COVID"; Diag = "You are not at high risk of having COVID".
