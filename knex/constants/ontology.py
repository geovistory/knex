from typing import List


class Klass:
    def __init__(self, pk_class: int, label:str):
        self.pk = pk_class
        self.label = label

    def __str__(self):
        return f'CLASS: pk {self.pk} - label "{self.label}"'

    @classmethod
    def find(self, pk:int=None, label:str=None):
        selection = list(filter(lambda klass: (pk != None and klass.pk == pk) or (label != None and str(label).lower() in klass.label.lower()), classes))
        if len(selection) == 0: raise Exception(f'Unknown class with parameter: pk:"{pk}" - text:"{label}"')
        if len(selection) == 1: return selection[0]
        raise Exception(f'Multiple classes found with parameter: pk:"{pk}" - text:"{label}"')


class Property:
    def __init__(self, pk_property: int, label:str):
        self.pk = pk_property
        self.label = label

    def __str__(self):
        return f'PROPERTY: pk {self.pk} - label "{self.label}"'

    @classmethod
    def find(self, pk:int=None, label:str=None):
        selection = list(filter(lambda property: (pk != None and property.pk == pk) or (label != None and str(label).lower in property.label.lower()), properties))
        if len(selection) == 0: raise Exception(f'Unknown property pk:"{pk}" ; text:"{label}"]')
        if len(selection) == 1: return selection[0]
        raise Exception(f'Multiple properties found with parameter: pk:"{pk}" - text:"{label}"')

classes: List[Klass] = [
    Klass(1, "CRM Entity"),
    Klass(2, "Temporal Entity"),
    Klass(5, "Event"),
    Klass(7, "Activity"),
    Klass(8, "Acquisition"),
    Klass(9, "Move"),
    Klass(11, "Modification"),
    Klass(12, "Production"),
    Klass(18, "Physical Thing"),
    Klass(21, "Person"),
    Klass(22, "Man-Made Object"),
    Klass(23, "Physical Human-Made Thing"),
    Klass(24, "Man-Made Feature"),
    Klass(32, "Linguistic Object"),
    Klass(35, "Visual Item"),
    Klass(38, "Actor"),
    Klass(39, "Legal Body"),
    Klass(40, "Appellation"),
    Klass(41, "Identifier"),
    Klass(50, "Time-Span"),
    Klass(51, "Place"),
    Klass(52, "Dimension"),
    Klass(53, "Type"),
    Klass(54, "Language"),
    Klass(55, "Material"),
    Klass(56, "Measurement Unit"),
    Klass(59, "Creation"),
    Klass(60, "Formation"),
    Klass(61, "Birth"),
    Klass(62, "Dissolution"),
    Klass(63, "Death"),
    Klass(65, "Human-Made Thing"),
    Klass(67, "Information Object"),
    Klass(68, "Group"),
    Klass(71, "Curated Holding"),
    Klass(72, "Part Addition"),
    Klass(73, "Part Removal"),
    Klass(76, "Type Creation"),
    Klass(78, "Joining"),
    Klass(79, "Leaving"),
    Klass(80, "Curation Activity"),
    Klass(81, "Propositional Object"),
    Klass(84, "Presence"),
    Klass(211, "Entity Quality"),
    Klass(212, "Geographical Location"),
    Klass(213, "Social Quality of an Actor"),
    Klass(217, "Work"),
    Klass(218, "Expression"),
    Klass(219, "Manifestation Product Type"),
    Klass(220, "Manifestation Singleton"),
    Klass(221, "Item"),
    Klass(234, "Serial Work"),
    Klass(244, "Expression Creation"),
    Klass(247, "Performance"),
    Klass(332, "Activity Type"),
    Klass(334, "Social Relationship"),
    Klass(335, "Time Primitive"),
    Klass(338, "Number"),
    Klass(339, "String"),
    Klass(340, "Physical Thing Life"),
    Klass(363, "Geographical Place"),
    Klass(364, "Geographical Place Type"),
    Klass(365, "Appellation in a Language"),
    Klass(369, "Observation"),
    Klass(374, "Property Type"),
    Klass(384, "Encounter Event"),
    Klass(388, "Excavation Process Unit"),
    Klass(389, "Stratigraphic Volume Unit"),
    Klass(390, "Stratigraphic Interface"),
    Klass(394, "Embedding"),
    Klass(396, "Archaeological Excavation"),
    Klass(441, "Construction"),
    Klass(442, "Membership"),
    Klass(443, "Construction Type"),
    Klass(444, "Actor's Social Quality"),
    Klass(445, "Argument"),
    Klass(449, "Geographical Location type"),
    Klass(450, "Manifestation Singleton Type"),
    Klass(451, "Group Type"),
    Klass(452, "Type of manifestation product type"),
    Klass(454, "Expression Type"),
    Klass(455, "[Geovistory] Digital"),
    Klass(456, "Chunk"),
    Klass(457, "Spot"),
    Klass(459, "Argument's method"),
    Klass(502, "Web Request"),
    Klass(503, "Expression portion"),
    Klass(516, "Expression Portion Type"),
    Klass(518, "Expression fragment"),
    Klass(519, "Item Type"),
    Klass(520, "Entity Quality Type"),
    Klass(521, "Cell"),
    Klass(522, "Ship"),
    Klass(523, "Ship Voyage"),
    Klass(524, "Ship Type"),
    Klass(525, "Shipyard"),
    Klass(526, "Economic good"),
    Klass(527, "Transport"),
    Klass(528, "Stopover"),
    Klass(529, "VOC Chamber"),
    Klass(533, "Shipbuilding"),
    Klass(535, "Participation"),
    Klass(607, "Web request type"),
    Klass(608, "Membership Type"),
    Klass(629, "Gender"),
    Klass(630, "Appellation in a Language Type"),
    Klass(631, "Pre-matrimonial enquiry"),
    Klass(632, "Social Relationship Type"),
    Klass(633, "Union"),
    Klass(634, "Type of Persons' Interaction"),
    Klass(635, "Tag"),
    Klass(636, "Occupation"),
    Klass(637, "Occupation (Temporal entity)"),
    Klass(638, "Marital status"),
    Klass(656, "Namespace"),
    Klass(657, "Reference"),
    Klass(664, "Pre-matrimonial enquiry motivation type"),
    Klass(676, "Expression Publication Event"),
    Klass(677, "Physical Human-Made Thing Type"),
    Klass(680, "Built Work"),
    Klass(681, "Morphological Building Section"),
    Klass(682, "Filled Morphological Building Section"),
    Klass(683, "Empty Morphological Building Section"),
    Klass(686, "Phase"),
    Klass(688, "Holding of a Right or Obligation"),
    Klass(689, "Duration"),
    Klass(690, "Time unit"),
    Klass(691, "Account of a journey or stay"),
    Klass(694, "Concept referred to in a journey's or stay's account"),
    Klass(695, "Frequency class"),
    Klass(696, "Epistemic Situation"),
    Klass(697, "Social Role Embodiment"),
    Klass(698, "Social Role"),
    Klass(701, "Custom or Law"),
    Klass(702, "Persons' Interaction"),
    Klass(704, "Being in Force"),
    Klass(705, "Custom or Law Type"),
    Klass(707, "Numeric dimension"),
    Klass(708, "Numeric dimension type"),
    Klass(709, "Length"),
    Klass(710, "Length measurement unit"),
    Klass(711, "Weight"),
    Klass(712, "Weight measurement unit"),
    Klass(713, "Area"),
    Klass(714, "Area measurement unit"),
    Klass(715, "Volume measurement unit"),
    Klass(716, "Volume"),
    Klass(717, "Monetary amount"),
    Klass(718, "Currency"),
    Klass(720, "Legal Quality Type"),
    Klass(721, "Procedure"),
    Klass(722, "Step"),
    Klass(723, "Component of a Recipe"),
    Klass(724, "Procedure Type"),
    Klass(725, "Step Type"),
    Klass(726, "Physical Component"),
    Klass(727, "Use"),
    Klass(728, "Use type"),
    Klass(752, "Intentional Collective"),
    Klass(758, "Religious Identity"),
    Klass(759, "Religion or Religious Denomination"),
    Klass(760, "Quantifiable Quality"),
    Klass(783, "Uniform Resource Locator (URL)"),
    Klass(784, "Short title"),
    Klass(785, "Text"),
    Klass(786, "Abstract individual"),
    Klass(787, "Political or Administrative Entity"),
    Klass(806, "Legal Quality"),
    Klass(807, "Legal Fact"),
    Klass(808, "Legal Location of an Actor"),
    Klass(826, "Identification"),
    Klass(827, "Identifier Type"),
    Klass(831, "Teaching"),
    Klass(837, "Unitary Event"),
    Klass(838, "Event Type"),
    Klass(839, "Phase Type"),
    Klass(840, "Archeological Excavation Type"),
    Klass(841, "Excavation Process Unit Type"),
    Klass(846, "Study"),
    Klass(847, "Legal Quality Acquisition"),
    Klass(848, "Actor's Legal Quality Acquisition Type"),
    Klass(849, "Obtaining a Study Title"),
    Klass(850, "Study title"),
    Klass(859, "Academic Discipline"),
    Klass(860, "Academic Chair"),
    Klass(861, "Academic Position"),
    Klass(866, "Holding of a Right Type"),
    Klass(867, "Asserted Actor's Role"),
    Klass(868, "Person Appellation in a Language"),
    Klass(869, "Person Appellation in a Language Type"),
    Klass(870, "Bibliographic Citation"),
    Klass(871, "Citation Style"),
    Klass(872, "Belonging to a Physical Collection"),
    Klass(873, "Collection Type"),
    Klass(874, "Manifestation Singleton Appellation Type"),
    Klass(879, "Taking Care of a Person"),
    Klass(880, "Attending a School"),
    Klass(881, "Intentional Entity"),
    Klass(882, "Social Role Type"),
    Klass(883, "Legal Location Type"),
    Klass(884, "Tanking Care of a Person Type"),
    Klass(885, "Attending a School Type"),
    Klass(887, "Intentional Event"),
    Klass(897, "Activity Domain"),
    Klass(898, "Table"),
    Klass(899, "Definition"),
    Klass(900, "Comment"),
    Klass(903, "Text type"),
    Klass(904, "Comment type"),
    Klass(933, "Annotation in Text"),
    Klass(934, "Annotation in Table"),
    Klass(935, "Mentioning"),
    Klass(936, "Table Value"),
    Klass(946, "Actor's Quality in Relation to an Event"),
    Klass(947, "Dimension Kind"),
    Klass(948, "Information Object Type"),
    Klass(955, "Dedication"),
    Klass(956, "Performance Type"),
    Klass(967, "Uniform Resource Identifier (URI)"),
    Klass(968, "Mentioning in Table"),
    Klass(969, "Relative Location of a Physical Thing"),
    Klass(971, "Relative Location Type"),
    Klass(973, "Physical Displacement"),
    Klass(1063, "Move Type"),
    Klass(1065, "Actor's Movement or Journey"),
    Klass(1066, "Stopover"),
    Klass(1067, "Stopover Type"),
    Klass(1068, "Actor's Movement or Journey Type"),
    Klass(1069, "Carrier's Journey"),
    Klass(1070, "Carrier's Journey Type"),
    Klass(1071, "Actor's Coerced Trip"),
    Klass(1072, "Actor's Coerced Trip Type"),
    Klass(1076, "Geographical Place Classification"),
    Klass(1077, "Observed Entity Type"),
    Klass(1150, "Asserted Datation"),
    Klass(1152, "Amount of Matter"),
    Klass(1210, "Geographical Place Kind"),
    Klass(1289, "Physical Set"),
    Klass(1290, "General Technique"),
    Klass(1295, "Asserted Datation Type"),
    Klass(1296, "Participation Type"),
    Klass(1358, "Intentional Collection of Physical Things"),
    Klass(1361, "Physical Human-Made Thing Classification"),
    Klass(1371, "Epistemic Situation Type"),
    Klass(1372, "Quantifiable Quality of a Spatio-Temporal Phenomenon"),
    Klass(1373, "Planned Move"),
    Klass(1374, "Quantifiable Component"),
    Klass(1375, "Quantifiable Component Type"),
    Klass(1377, "Quantifiable Quality of an Epistemic Situation"),
    Klass(1378, "Thing Involved in an Epistemic Situation"),
    Klass(1379, "Type of Involvement of a Thing in an Epistemic Situation"),
    Klass(1380, "Link"),
    Klass(1381, "Link Type"),
    Klass(1383, "Activity Purpose"),
    Klass(1384, "Event Classification"),
    Klass(1385, "Event Classification Type"),
    Klass(1431, "Participation Relation"),
    Klass(1432, "Participation Relation Type"),
    Klass(1433, "Role in Participation Relation"),
    Klass(1491, "Political or Administrative Entity Type"),
]

class_E1_crmEntity = 1
class_E2_temporalEntity = 2
class_E5_event = 5
class_E7_activity = 7
class_E8_acquisition = 8
class_E9_move = 9
class_E11_modification = 11
class_E12_production = 12
class_E18_physicalThing = 18
class_E21_person = 21
class_E22_manMadeObject = 22
class_E24_physicalHumanMadeThing = 23
class_E25_manMadeFeature = 24
class_E33_linguisticObject = 32
class_E36_visualItem = 35
class_E39_actor = 38
class_E40_legalBody = 39
class_E41_appellation = 40
class_E42_identifier = 41
class_E52_timeSpan = 50
class_E53_place = 51
class_E54_dimension = 52
class_E55_type = 53
class_E56_language = 54
class_E57_material = 55
class_E58_measurementUnit = 56
class_E65_creation = 59
class_E66_formation = 60
class_E67_birth = 61
class_E68_dissolution = 62
class_E69_death = 63
class_E71_humanMadeThing = 65
class_E73_informationObject = 67
class_E74_group = 68
class_E78_curatedHolding = 71
class_E79_partAddition = 72
class_E80_partRemoval = 73
class_E83_typeCreation = 76
class_E85_joining = 78
class_E86_leaving = 79
class_E87_curationActivity = 80
class_E89_propositionalObject = 81
class_E93_presence = 84
class_C1_entityQuality = 211
class_C15_geographicalLocation = 212
class_C1_socialQualityOfAnActor = 213
class_F1_work = 217
class_F2_expression = 218
class_F3_manifestationProductType = 219
class_F4_manifestationSingleton = 220
class_F5_item = 221
class_F18_serialWork = 234
class_F28_expressionCreation = 244
class_F31_performance = 247
class_C3_activityType = 332
class_C3_socialRelationship = 334
class_E61_timePrimitive = 335
class_E60_number = 338
class_E62_string = 339
class_C19_physicalThingLife = 340
class_C13_geographicalPlace = 363
class_C14_geographicalPlaceType = 364
class_C11_appellationInALanguage = 365
class_S4_observation = 369
class_S9_propertyType = 374
class_S19_encounterEvent = 384
class_A1_excavationProcessUnit = 388
class_A2_stratigraphicVolumeUnit = 389
class_A3_stratigraphicInterface = 390
class_A7_embedding = 394
class_A9_archaeologicalExcavation = 396
class_C17_construction = 441
class_C5_membership = 442
class_C18_constructionType = 443
class_C2_actorsSocialQuality = 444
class_C12_argument = 445
class_C16_geographicalLocationType = 449
class_C10_manifestationSingletonType = 450
class_C9_groupType = 451
class_C8_typeOfManifestationProductType = 452
class_C6_expressionType = 454
class_C1_geovistoryDigital = 455
class_C2_chunk = 456
class_C3_spot = 457
class_C13_argumentsMethod = 459
class_C4_webRequest = 502
class_C2_expressionPortion = 503
class_C3_expressionPortionType = 516
class_C6_expressionFragment = 518
class_C5_itemType = 519
class_C20_entityQualityType = 520
class_C7_cell = 521
class_C2_ship = 522
class_C1_shipVoyage = 523
class_C3_shipType = 524
class_C4_shipyard = 525
class_C5_economicGood = 526
class_C6_transport = 527
class_C7_stopover = 528
class_C8_vocChamber = 529
class_C12_shipbuilding = 533
class_C15_participation = 535
class_C8_webRequestType = 607
class_C6_membershipType = 608
class_C11_gender = 629
class_C12_appellationInALanguageType = 630
class_C1_preMatrimonialEnquiry = 631
class_C4_socialRelationshipType = 632
class_C9_union = 633
class_C10_typeOfPersonsInteraction = 634
class_C9_tag = 635
class_C7_occupation = 636
class_C8_occupationTemporalEntity = 637
class_C2_maritalStatus = 638
class_C10_namespace = 656
class_C11_reference = 657
class_C3_preMatrimonialEnquiryMotivationType = 664
class_C1_expressionPublicationEvent = 676
class_C4_physicalHumanMadeThingType = 677
class_B1_builtWork = 680
class_B2_morphologicalBuildingSection = 681
class_B3_filledMorphologicalBuildingSection = 682
class_B4_emptyMorphologicalBuildingSection = 683
class_C4_phase = 686
class_C14_holdingOfARightOrObligation = 688
class_C1_duration = 689
class_C2_timeUnit = 690
class_C4_accountOfAJourneyOrStay = 691
class_C5_conceptReferredToInAJourneysOrStaysAccount = 694
class_C6_frequencyClass = 695
class_C3_epistemicSituation = 696
class_C13_socialRoleEmbodiment = 697
class_C12_socialRole = 698
class_C17_customOrLaw = 701
class_C18_personsInteraction = 702
class_C20_beingInForce = 704
class_C21_customOrLawType = 705
class_C11_numericDimension = 707
class_C12_numericDimensionType = 708
class_C13_length = 709
class_C14_lengthMeasurementUnit = 710
class_C15_weight = 711
class_C16_weightMeasurementUnit = 712
class_C17_area = 713
class_C18_areaMeasurementUnit = 714
class_C19_volumeMeasurementUnit = 715
class_C20_volume = 716
class_C21_monetaryAmount = 717
class_C22_currency = 718
class_C22_legalQualityType = 720
class_C4_procedure = 721
class_C5_step = 722
class_C6_componentOfARecipe = 723
class_C7_procedureType = 724
class_C8_stepType = 725
class_C22_physicalComponent = 726
class_C23_use = 727
class_C24_useType = 728
class_C25_intentionalCollective = 752
class_C23_religiousIdentity = 758
class_C24_religionOrReligiousDenomination = 759
class_C28_quantifiableQuality = 760
class_C14_uniformResourceLocatorUrl = 783
class_C15_shortTitle = 784
class_C16_text = 785
class_C32_abstractIndividual = 786
class_C25_politicalOrAdministrativeEntity = 787
class_C26_legalQuality = 806
class_C27_legalFact = 807
class_C28_legalLocationOfAnActor = 808
class_C23_identification = 826
class_C24_identifierType = 827
class_C1_teaching = 831
class_C33_unitaryEvent = 837
class_C34_eventType = 838
class_C35_phaseType = 839
class_C1_archeologicalExcavationType = 840
class_C2_excavationProcessUnitType = 841
class_C2_study = 846
class_C29_legalQualityAcquisition = 847
class_C30_actorsLegalQualityAcquisitionType = 848
class_C3_obtainingAStudyTitle = 849
class_C4_studyTitle = 850
class_C5_academicDiscipline = 859
class_C6_academicChair = 860
class_C7_academicPosition = 861
class_C31_holdingOfARightType = 866
class_C9_assertedActorsRole = 867
class_C38_personAppellationInALanguage = 868
class_C39_personAppellationInALanguageType = 869
class_C10_bibliographicCitation = 870
class_C11_citationStyle = 871
class_C27_belongingToAPhysicalCollection = 872
class_C26_collectionType = 873
class_C17_manifestationSingletonAppellationType = 874
class_C1_takingCareOfAPerson = 879
class_C2_attendingASchool = 880
class_C9_intentionalEntity = 881
class_C32_socialRoleType = 882
class_C33_legalLocationType = 883
class_C3_tankingCareOfAPersonType = 884
class_C4_attendingASchoolType = 885
class_C10_intentionalEvent = 887
class_C34_activityDomain = 897
class_C18_table = 898
class_C19_definition = 899
class_C20_comment = 900
class_C23_textType = 903
class_C24_commentType = 904
class_C26_annotationInText = 933
class_C27_annotationInTable = 934
class_C28_mentioning = 935
class_C29_tableValue = 936
class_C35_actorsQualityInRelationToAnEvent = 946
class_C27_dimensionKind = 947
class_C28_informationObjectType = 948
class_C12_dedication = 955
class_C29_performanceType = 956
class_C30_uniformResourceIdentifierUri = 967
class_C31_mentioningInTable = 968
class_C41_relativeLocationOfAPhysicalThing = 969
class_C43_relativeLocationType = 971
class_C45_physicalDisplacement = 973
class_C31_moveType = 1063
class_C1_actorsMovementOrJourney = 1065
class_C2_stopover = 1066
class_C3_stopoverType = 1067
class_C4_actorsMovementOrJourneyType = 1068
class_C5_carriersJourney = 1069
class_C6_carriersJourneyType = 1070
class_C7_actorsCoercedTrip = 1071
class_C8_actorsCoercedTripType = 1072
class_C48_geographicalPlaceClassification = 1076
class_C32_observedEntityType = 1077
class_C13_assertedDatation = 1150
class_C49_amountOfMatter = 1152
class_C51_geographicalPlaceKind = 1210
class_C52_physicalSet = 1289
class_C53_generalTechnique = 1290
class_C14_assertedDatationType = 1295
class_C36_participationType = 1296
class_C54_intentionalCollectionOfPhysicalThings = 1358
class_C55_physicalHumanMadeThingClassification = 1361
class_C56_epistemicSituationType = 1371
class_C57_quantifiableQualityOfASpatioTemporalPhenomenon = 1372
class_C15_plannedMove = 1373
class_C16_quantifiableComponent = 1374
class_C17_quantifiableComponentType = 1375
class_C59_quantifiableQualityOfAnEpistemicSituation = 1377
class_C60_thingInvolvedInAnEpistemicSituation = 1378
class_C61_typeOfInvolvementOfAThingInAnEpistemicSituation = 1379
class_C62_link = 1380
class_C63_linkType = 1381
class_C34_activityPurpose = 1383
class_C64_eventClassification = 1384
class_C65_eventClassificationType = 1385
class_C39_participationRelation = 1431
class_C40_participationRelationType = 1432
class_C41_roleInParticipationRelation = 1433
class_C42_politicalOrAdministrativeEntityType = 1491

properties = [
    Property(1, "is identified by"),
    Property(2, "has type"),
    Property(4, "has time-span"),
    Property(7, "took place on or within"),
    Property(8, "consists of"),
    Property(10, "had participant"),
    Property(11, "occurred in the presence of"),
    Property(13, "carried out by"),
    Property(15, "used specific object"),
    Property(18, "had specific purpose"),
    Property(19, "had general purpose"),
    Property(20, "transferred title to"),
    Property(21, "transferred title from"),
    Property(22, "transferred title of"),
    Property(29, "has modified"),
    Property(30, "used general technique"),
    Property(40, "has dimension"),
    Property(42, "consists of"),
    Property(43, "is composed of"),
    Property(57, "shows visual item"),
    Property(63, "has language"),
    Property(71, "ongoing throughout"),
    Property(72, "at some time within"),
    Property(77, "falls within"),
    Property(78, "has value"),
    Property(79, "has unit"),
    Property(82, "has created"),
    Property(83, "has formed"),
    Property(84, "by mother"),
    Property(85, "from father"),
    Property(86, "brought into life"),
    Property(87, "dissolved"),
    Property(88, "was death of"),
    Property(89, "had as general use"),
    Property(96, "has produced"),
    Property(98, "augmented"),
    Property(99, "added"),
    Property(105, "occurs during"),
    Property(106, "overlaps in time with"),
    Property(107, "meets in time with"),
    Property(108, "occurs before"),
    Property(115, "has broader term"),
    Property(116, "carries"),
    Property(117, "is about"),
    Property(120, "spatiotemporally overlaps with"),
    Property(122, "continued"),
    Property(126, "represents"),
    Property(131, "joined"),
    Property(132, "joined with"),
    Property(133, "separated"),
    Property(134, "separated from"),
    Property(135, "curated"),
    Property(136, "has component"),
    Property(139, "was formed from"),
    Property(145, "is temporally specified by"),
    Property(146, "incorporates"),
    Property(147, "was a presence of"),
    Property(148, "was within"),
    Property(150, "end of the begin"),
    Property(151, "begin of the end"),
    Property(152, "begin of the begin"),
    Property(153, "end of the end"),
    Property(979, "carriers provided by"),
    Property(982, "is example of"),
    Property(991, "created"),
    Property(992, "created"),
    Property(993, "created a realisation of"),
    Property(1015, "has representative manifestation product type"),
    Property(1016, "is representative manifestation singleton for"),
    Property(1039, "included performed version of"),
    Property(1040, "effects"),
    Property(1041, "ends"),
    Property(1042, "has quantifiable quality"),
    Property(1066, "has location type"),
    Property(1075, "observed property type"),
    Property(1078, "has dimension"),
    Property(1085, "encountered object"),
    Property(1087, "has found at"),
    Property(1095, "removed part or all of"),
    Property(1106, "is found by"),
    Property(1107, "is embedding of"),
    Property(1108, "is embedding in"),
    Property(1109, "is embedding at"),
    Property(1110, "has geographical place type"),
    Property(1111, "is appellation for language of"),
    Property(1112, "used in language"),
    Property(1113, "refers to name"),
    Property(1177, "was location of"),
    Property(1178, "is location at"),
    Property(1183, "at distance"),
    Property(1188, "was a membership of"),
    Property(1189, "was membership in"),
    Property(1190, "has built work type"),
    Property(1203, "has event type"),
    Property(1204, "has group type"),
    Property(1205, "has manifestation singleton type"),
    Property(1206, "has type of manifestation product type"),
    Property(1214, "has expression type"),
    Property(1216, "is reproduction of"),
    Property(1246, "has argument method"),
    Property(1305, "is server response to request"),
    Property(1316, "has carrier provided by"),
    Property(1317, "is part of"),
    Property(1320, "has expression portion type"),
    Property(1321, "has item type"),
    Property(1323, "has web request type"),
    Property(1334, "refers to"),
    Property(1335, "had departure place"),
    Property(1336, "had arrival place"),
    Property(1337, "has ship type"),
    Property(1338, "was carried out by"),
    Property(1339, "took place at"),
    Property(1340, "was part of"),
    Property(1341, "has built"),
    Property(1342, "carried out by"),
    Property(1343, "is carried out in the context of"),
    Property(1344, "is participation of"),
    Property(1345, "is participation in"),
    Property(1346, "is participation in the quality of"),
    Property(1354, "has set up"),
    Property(1355, "same as entity"),
    Property(1357, "is part of"),
    Property(1358, "carried"),
    Property(1359, "participated in"),
    Property(1409, "involves partner"),
    Property(1410, "has quality type"),
    Property(1411, "pertains to"),
    Property(1412, "has social quality"),
    Property(1413, "has membership type"),
    Property(1414, "is life of"),
    Property(1429, "has gender"),
    Property(1430, "has appellation for language type"),
    Property(1431, "the investigation concerns"),
    Property(1432, "is requested as a witness"),
    Property(1433, "is documented in"),
    Property(1434, "has relationship type"),
    Property(1435, "stemmed from"),
    Property(1436, "had partner"),
    Property(1437, "has type of interaction"),
    Property(1439, "has its origins in"),
    Property(1440, "tagged by"),
    Property(1441, "is occupation of"),
    Property(1442, "is about"),
    Property(1443, "takes place at"),
    Property(1444, "on behalf of"),
    Property(1445, "has relationship source"),
    Property(1446, "has relationship target"),
    Property(1499, "has to be merged with"),
    Property(1500, "belongs to"),
    Property(1516, "has motivation"),
    Property(1517, "has motivation type"),
    Property(1595, "used specific expression"),
    Property(1596, "created manifestation"),
    Property(1597, "published the work of"),
    Property(1598, "has type"),
    Property(1599, "took place at"),
    Property(1600, "is section of"),
    Property(1609, "is defined in relation to"),
    Property(1610, "is subjection of"),
    Property(1611, "is right of"),
    Property(1612, "has time unit"),
    Property(1613, "has duration"),
    Property(1616, "mentions geographical place"),
    Property(1617, "concerns"),
    Property(1618, "has time lapse before account"),
    Property(1619, "refers to"),
    Property(1620, "has frequency classification"),
    Property(1621, "has as a minimum duration"),
    Property(1622, "has as a maximum duration"),
    Property(1623, "has time lapse of last journey before account"),
    Property(1626, "is embodiment by"),
    Property(1627, "has marital status"),
    Property(1630, "has holding of a right type"),
    Property(1631, "is validity of"),
    Property(1632, "realizes"),
    Property(1633, "has custom or law type"),
    Property(1634, "is embodiment of"),
    Property(1635, "has numeric dimension type"),
    Property(1636, "has measurement unit"),
    Property(1637, "has measurement unit"),
    Property(1638, "has measurement unit"),
    Property(1639, "has measurement unit"),
    Property(1640, "has currency"),
    Property(1641, "is intention of"),
    Property(1642, "is participation on behalf of"),
    Property(1643, "is defined by"),
    Property(1644, "requires the use of"),
    Property(1645, "has material"),
    Property(1646, "has volume"),
    Property(1647, "has planned duration"),
    Property(1648, "has weight"),
    Property(1649, "shall be performed after"),
    Property(1650, "has step type"),
    Property(1651, "has procedure type"),
    Property(1652, "foresees the use of specific object"),
    Property(1653, "effects"),
    Property(1654, "ends"),
    Property(1655, "belongs to"),
    Property(1656, "has part"),
    Property(1657, "is composed of part of type"),
    Property(1658, "has use type"),
    Property(1659, "is use by"),
    Property(1660, "has purpose"),
    Property(1661, "is use of"),
    Property(1739, "pertains to"),
    Property(1742, "has quality dimension"),
    Property(1759, "has setting"),
    Property(1760, "has web address"),
    Property(1761, "has short title"),
    Property(1762, "has definition"),
    Property(1763, "has comment"),
    Property(1777, "involves legal quality"),
    Property(1778, "has legal connotation type"),
    Property(1779, "has type"),
    Property(1780, "is valid in"),
    Property(1781, "is valid identifier of"),
    Property(1782, "is identification of"),
    Property(1783, "has identifier type"),
    Property(1784, "is interaction of"),
    Property(1785, "has maximal projection in geographical space"),
    Property(1797, "has activity type"),
    Property(1798, "is identified by"),
    Property(1799, "has archeological excavation type"),
    Property(1801, "has excavation process unit type"),
    Property(1802, "overlies"),
    Property(1803, "cuts"),
    Property(1805, "is study at"),
    Property(1806, "is the study by"),
    Property(1807, "is acquisition by"),
    Property(1808, "is acquisition of"),
    Property(1809, "issued by"),
    Property(1810, "has legal quality acquisition type"),
    Property(1811, "was obtained by"),
    Property(1812, "is obtention of"),
    Property(1815, "has academic supervisor"),
    Property(1826, "concerns"),
    Property(1827, "is carried out by"),
    Property(1828, "carried out at"),
    Property(1829, "has rank"),
    Property(1830, "has as disciplinary area"),
    Property(1831, "is delivered by"),
    Property(1832, "is study of"),
    Property(1833, "is obtained at"),
    Property(1837, "is role of"),
    Property(1838, "is asserted by"),
    Property(1839, "is qualified by"),
    Property(1840, "is in the role of"),
    Property(1841, "has style"),
    Property(1842, "same as external identifier"),
    Property(1843, "has value"),
    Property(1844, "is about"),
    Property(1846, "has preferred type"),
    Property(1847, "take care of"),
    Property(1848, "has caretaker"),
    Property(1849, "concerned person"),
    Property(1850, "concerned school"),
    Property(1851, "has specific location"),
    Property(1852, "has location"),
    Property(1853, "has social role type"),
    Property(1854, "has legal location type"),
    Property(1855, "has taking care type"),
    Property(1856, "has attending a school type"),
    Property(1857, "is legal connotation of"),
    Property(1863, "belongs to activity domain"),
    Property(1864, "has value version"),
    Property(1865, "has text type"),
    Property(1866, "has comment type"),
    Property(1872, "is annotated in"),
    Property(1874, "at position"),
    Property(1875, "annotated entity"),
    Property(1876, "mentions"),
    Property(1877, "is mentioned in"),
    Property(1878, "at position"),
    Property(1879, "has value"),
    Property(1881, "is location in or on"),
    Property(1887, "has issue"),
    Property(1889, "is about"),
    Property(1892, "has intermediary"),
    Property(1893, "is quality in relation to"),
    Property(1894, "has dimension kind"),
    Property(1895, "has information object type"),
    Property(1922, "effects dedication"),
    Property(1923, "has dedicatory object"),
    Property(1924, "has dedicatee"),
    Property(1925, "has conceptual dedicatee"),
    Property(1926, "has beneficiary"),
    Property(1927, "is about"),
    Property(1928, "is quality of"),
    Property(1930, "is quality on behalf of"),
    Property(1931, "has performance type"),
    Property(1943, "same as URI [owl:sameAs]"),
    Property(1944, "is in relation to"),
    Property(1945, "is inside or relative to"),
    Property(1946, "has relative location type"),
    Property(1947, "is quality of"),
    Property(2109, "moved from"),
    Property(2110, "moved to"),
    Property(2111, "displaces"),
    Property(2112, "has move identifying type"),
    Property(2116, "is movement of"),
    Property(2117, "has movement identifying type"),
    Property(2118, "has stopover identifying type"),
    Property(2119, "is journey of"),
    Property(2120, "has carrier's journey identifying type"),
    Property(2121, "is coerced displacement of"),
    Property(2122, "has actor's coerced trip identifying type"),
    Property(2123, "is continuation of"),
    Property(2124, "classifies"),
    Property(2125, "classifies with"),
    Property(2128, "observed entity type"),
    Property(2214, "has datation value"),
    Property(2257, "was or is composed of object of type"),
    Property(2270, "has quality during membership"),
    Property(2272, "has asserted datation type"),
    Property(2274, "has type of participation"),
    Property(2283, "could be the same entity as"),
    Property(2299, "classifies"),
    Property(2300, "classifies with"),
    Property(2310, "has epistemic situation preferred type"),
    Property(2311, "is quantifiable quality of"),
    Property(2312, "planned move from"),
    Property(2313, "planned move to"),
    Property(2314, "has component dimension"),
    Property(2315, "has quantifiable component type"),
    Property(2316, "is quantifiable quality of"),
    Property(2317, "is involvement in"),
    Property(2318, "has involvement type"),
    Property(2319, "is involvement of"),
    Property(2320, "is linked to"),
    Property(2321, "has link type"),
    Property(2324, "classifies"),
    Property(2325, "classifies with"),
    Property(2368, "has participation relation type"),
    Property(2369, "is participation relation of"),
    Property(2370, "has participation relation role"),
    Property(2371, "has role quality"),
    Property(2415, "has mentioning content"),
    Property(2416, "is defined in the context of"),
    Property(2436, "is embodied in"),
    Property(2437, "has political or administrative entity type"),
]

property_P1_isIdentifiedBy = 1
property_P2_hasType = 2
property_P4_hasTimeSpan = 4
property_P8_tookPlaceOnOrWithin = 7
property_P9_consistsOf = 8
property_P11_hadParticipant = 10
property_P12_occurredInThePresenceOf = 11
property_P14_carriedOutBy = 13
property_P16_usedSpecificObject = 15
property_P20_hadSpecificPurpose = 18
property_P21_hadGeneralPurpose = 19
property_P22_transferredTitleTo = 20
property_P23_transferredTitleFrom = 21
property_P24_transferredTitleOf = 22
property_P31_hasModified = 29
property_P32_usedGeneralTechnique = 30
property_P43_hasDimension = 40
property_P45_consistsOf = 42
property_P46_isComposedOf = 43
property_P65_showsVisualItem = 57
property_P72_hasLanguage = 63
property_P81_ongoingThroughout = 71
property_P82_atSomeTimeWithin = 72
property_P89_fallsWithin = 77
property_P90_hasValue = 78
property_P91_hasUnit = 79
property_P94_hasCreated = 82
property_P95_hasFormed = 83
property_P96_byMother = 84
property_P97_fromFather = 85
property_P98_broughtIntoLife = 86
property_P99_dissolved = 87
property_P100_wasDeathOf = 88
property_P101_hadAsGeneralUse = 89
property_P108_hasProduced = 96
property_P110_augmented = 98
property_P111_added = 99
property_P117_occursDuring = 105
property_P118_overlapsInTimeWith = 106
property_P119_meetsInTimeWith = 107
property_P120_occursBefore = 108
property_P127_hasBroaderTerm = 115
property_P128_carries = 116
property_P129_isAbout = 117
property_P132_spatiotemporallyOverlapsWith = 120
property_P134_continued = 122
property_P138_represents = 126
property_P143_joined = 131
property_P144_joinedWith = 132
property_P145_separated = 133
property_P146_separatedFrom = 134
property_P147_curated = 135
property_P148_hasComponent = 136
property_P151_wasFormedFrom = 139
property_P164_isTemporallySpecifiedBy = 145
property_P165_incorporates = 146
property_P166_wasAPresenceOf = 147
property_P167_wasWithin = 148
property_P81a_endOfTheBegin = 150
property_P81b_beginOfTheEnd = 151
property_P82a_beginOfTheBegin = 152
property_P82b_endOfTheEnd = 153
property_R4_carriersProvidedBy = 979
property_R7_isExampleOf = 982
property_R17_created = 991
property_R18_created = 992
property_R19_createdARealisationOf = 993
property_R41_hasRepresentativeManifestationProductType = 1015
property_R42_isRepresentativeManifestationSingletonFor = 1016
property_R66_includedPerformedVersionOf = 1039
property_P3_effects = 1040
property_P4_ends = 1041
property_P22_hasQuantifiableQuality = 1042
property_P19_hasLocationType = 1066
property_O9_observedPropertyType = 1075
property_O12_hasDimension = 1078
property_O19_encounteredObject = 1085
property_O21_hasFoundAt = 1087
property_AP5_removedPartOrAllOf = 1095
property_AP17_isFoundBy = 1106
property_AP18_isEmbeddingOf = 1107
property_AP19_isEmbeddingIn = 1108
property_AP20_isEmbeddingAt = 1109
property_P20_hasGeographicalPlaceType = 1110
property_P11_isAppellationForLanguageOf = 1111
property_P12_usedInLanguage = 1112
property_P13_refersToName = 1113
property_P17_wasLocationOf = 1177
property_P15_isLocationAt = 1178
property_P16_atDistance = 1183
property_P1_wasAMembershipOf = 1188
property_P2_wasMembershipIn = 1189
property_P9_hasBuiltWorkType = 1190
property_P47_hasEventType = 1203
property_P7_hasGroupType = 1204
property_P6_hasManifestationSingletonType = 1205
property_P5_hasTypeOfManifestationProductType = 1206
property_P4_hasExpressionType = 1214
property_P1_isReproductionOf = 1216
property_P15_hasArgumentMethod = 1246
property_P4_isServerResponseToRequest = 1305
property_P5_hasCarrierProvidedBy = 1316
property_P4_isPartOf = 1317
property_P5_hasExpressionPortionType = 1320
property_P2_hasItemType = 1321
property_P8_hasWebRequestType = 1323
property_P9_refersTo = 1334
property_P1_hadDeparturePlace = 1335
property_P2_hadArrivalPlace = 1336
property_P6_hasShipType = 1337
property_P3_wasCarriedOutBy = 1338
property_P4_tookPlaceAt = 1339
property_P5_wasPartOf = 1340
property_P7_hasBuilt = 1341
property_P8_carriedOutBy = 1342
property_P9_isCarriedOutInTheContextOf = 1343
property_P10_isParticipationOf = 1344
property_P11_isParticipationIn = 1345
property_P12_isParticipationInTheQualityOf = 1346
property_P10_hasSetUp = 1354
property_P10_sameAsEntity = 1355
property_P5_isPartOf = 1357
property_P11_carried = 1358
property_P12_participatedIn = 1359
property_P15_involvesPartner = 1409
property_P23_hasQualityType = 1410
property_P13_pertainsTo = 1411
property_P14_hasSocialQuality = 1412
property_P3_hasMembershipType = 1413
property_P26_isLifeOf = 1414
property_P23_hasGender = 1429
property_P14_hasAppellationForLanguageType = 1430
property_P1_theInvestigationConcerns = 1431
property_P2_isRequestedAsAWitness = 1432
property_P3_isDocumentedIn = 1433
property_P16_hasRelationshipType = 1434
property_P22_stemmedFrom = 1435
property_P20_hadPartner = 1436
property_P21_hasTypeOfInteraction = 1437
property_P24_hasItsOriginsIn = 1439
property_P12_taggedBy = 1440
property_P4_isOccupationOf = 1441
property_P5_isAbout = 1442
property_P6_takesPlaceAt = 1443
property_P7_onBehalfOf = 1444
property_P17_hasRelationshipSource = 1445
property_P18_hasRelationshipTarget = 1446
property_P13_hasToBeMergedWith = 1499
property_P14_belongsTo = 1500
property_P4_hasMotivation = 1516
property_P5_hasMotivationType = 1517
property_P1_usedSpecificExpression = 1595
property_P2_createdManifestation = 1596
property_P3_publishedTheWorkOf = 1597
property_P1_hasType = 1598
property_P6_tookPlaceAt = 1599
property_BP1_isSectionOf = 1600
property_P19_isDefinedInRelationTo = 1609
property_P8_isSubjectionOf = 1610
property_P9_isRightOf = 1611
property_P10_hasTimeUnit = 1612
property_P6_hasDuration = 1613
property_P7_mentionsGeographicalPlace = 1616
property_P8_concerns = 1617
property_P9_hasTimeLapseBeforeAccount = 1618
property_P10_refersTo = 1619
property_P11_hasFrequencyClassification = 1620
property_P12_hasAsAMinimumDuration = 1621
property_P13_hasAsAMaximumDuration = 1622
property_P14_hasTimeLapseOfLastJourneyBeforeAccount = 1623
property_P26_isEmbodimentBy = 1626
property_P15_hasMaritalStatus = 1627
property_P29_hasHoldingOfARightType = 1630
property_P30_isValidityOf = 1631
property_P31_realizes = 1632
property_P32_hasCustomOrLawType = 1633
property_P33_isEmbodimentOf = 1634
property_P11_hasNumericDimensionType = 1635
property_P12_hasMeasurementUnit = 1636
property_P13_hasMeasurementUnit = 1637
property_P14_hasMeasurementUnit = 1638
property_P15_hasMeasurementUnit = 1639
property_P16_hasCurrency = 1640
property_P7_isIntentionOf = 1641
property_P34_isParticipationOnBehalfOf = 1642
property_P35_isDefinedBy = 1643
property_P6_requiresTheUseOf = 1644
property_P7_hasMaterial = 1645
property_P8_hasVolume = 1646
property_P9_hasPlannedDuration = 1647
property_P10_hasWeight = 1648
property_P11_shallBePerformedAfter = 1649
property_P12_hasStepType = 1650
property_P13_hasProcedureType = 1651
property_P14_foreseesTheUseOfSpecificObject = 1652
property_P8_effects = 1653
property_P9_ends = 1654
property_P27_belongsTo = 1655
property_P28_hasPart = 1656
property_P17_isComposedOfPartOfType = 1657
property_P29_hasUseType = 1658
property_P30_isUseBy = 1659
property_P31_hasPurpose = 1660
property_P32_isUseOf = 1661
property_P36_pertainsTo = 1739
property_P35_hasQualityDimension = 1742
property_P43_hasSetting = 1759
property_P16_hasWebAddress = 1760
property_P17_hasShortTitle = 1761
property_P18_hasDefinition = 1762
property_P19_hasComment = 1763
property_P37_involvesLegalQuality = 1777
property_P38_hasLegalConnotationType = 1778
property_P39_hasType = 1779
property_P40_isValidIn = 1780
property_P18_isValidIdentifierOf = 1781
property_P18_isIdentificationOf = 1782
property_P19_hasIdentifierType = 1783
property_P41_isInteractionOf = 1784
property_P45_hasMaximalProjectionInGeographicalSpace = 1785
property_P19_hasActivityType = 1797
property_P46_isIdentifiedBy = 1798
property_P1_hasArcheologicalExcavationType = 1799
property_P2_hasExcavationProcessUnitType = 1801
property_P3_overlies = 1802
property_P4_cuts = 1803
property_P1_isStudyAt = 1805
property_P2_isTheStudyBy = 1806
property_P43_isAcquisitionBy = 1807
property_P44_isAcquisitionOf = 1808
property_P45_issuedBy = 1809
property_P46_hasLegalQualityAcquisitionType = 1810
property_P3_wasObtainedBy = 1811
property_P4_isObtentionOf = 1812
property_P5_hasAcademicSupervisor = 1815
property_P6_concerns = 1826
property_P7_isCarriedOutBy = 1827
property_P8_carriedOutAt = 1828
property_P9_hasRank = 1829
property_P10_hasAsDisciplinaryArea = 1830
property_P11_isDeliveredBy = 1831
property_P12_isStudyOf = 1832
property_P13_isObtainedAt = 1833
property_P15_isRoleOf = 1837
property_P16_isAssertedBy = 1838
property_P17_isQualifiedBy = 1839
property_P18_isInTheRoleOf = 1840
property_P19_hasStyle = 1841
property_P20_sameAsExternalIdentifier = 1842
property_P21_hasValue = 1843
property_P55_isAbout = 1844
property_P63_hasPreferredType = 1846
property_P1_takeCareOf = 1847
property_P2_hasCaretaker = 1848
property_P3_concernedPerson = 1849
property_P4_concernedSchool = 1850
property_P48_hasSpecificLocation = 1851
property_P49_hasLocation = 1852
property_P50_hasSocialRoleType = 1853
property_P51_hasLegalLocationType = 1854
property_P5_hasTakingCareType = 1855
property_P6_hasAttendingASchoolType = 1856
property_P52_isLegalConnotationOf = 1857
property_P55_belongsToActivityDomain = 1863
property_P20_hasValueVersion = 1864
property_P21_hasTextType = 1865
property_P22_hasCommentType = 1866
property_P23_isAnnotatedIn = 1872
property_P24_atPosition = 1874
property_P25_annotatedEntity = 1875
property_P26_mentions = 1876
property_P27_isMentionedIn = 1877
property_P28_atPosition = 1878
property_P29_hasValue = 1879
property_P52_isLocationInOrOn = 1881
property_P20_hasIssue = 1887
property_P30_isAbout = 1889
property_P16_hasIntermediary = 1892
property_P57_isQualityInRelationTo = 1893
property_P25_hasDimensionKind = 1894
property_P26_hasInformationObjectType = 1895
property_P21_effectsDedication = 1922
property_P22_hasDedicatoryObject = 1923
property_P23_hasDedicatee = 1924
property_P24_hasConceptualDedicatee = 1925
property_P25_hasBeneficiary = 1926
property_P58_isAbout = 1927
property_P59_isQualityOf = 1928
property_P61_isQualityOnBehalfOf = 1930
property_P27_hasPerformanceType = 1931
property_P28_sameAsUriOwlSameas = 1943
property_P62_isInRelationTo = 1944
property_P57_isInsideOrRelativeTo = 1945
property_P58_hasRelativeLocationType = 1946
property_P59_isQualityOf = 1947
property_P60_movedFrom = 2109
property_P61_movedTo = 2110
property_P62_displaces = 2111
property_P29_hasMoveIdentifyingType = 2112
property_P1_isMovementOf = 2116
property_P2_hasMovementIdentifyingType = 2117
property_P3_hasStopoverIdentifyingType = 2118
property_P4_isJourneyOf = 2119
property_P5_hasCarriersJourneyIdentifyingType = 2120
property_P6_isCoercedDisplacementOf = 2121
property_P7_hasActorsCoercedTripIdentifyingType = 2122
property_P8_isContinuationOf = 2123
property_P68_classifies = 2124
property_P64_classifiesWith = 2125
property_P30_observedEntityType = 2128
property_P26_hasDatationValue = 2214
property_P66_wasOrIsComposedOfObjectOfType = 2257
property_P63_hasQualityDuringMembership = 2270
property_P27_hasAssertedDatationType = 2272
property_P64_hasTypeOfParticipation = 2274
property_P71_couldBeTheSameEntityAs = 2283
property_P72_classifies = 2299
property_P73_classifiesWith = 2300
property_P74_hasEpistemicSituationPreferredType = 2310
property_P75_isQuantifiableQualityOf = 2311
property_P28_plannedMoveFrom = 2312
property_P29_plannedMoveTo = 2313
property_P30_hasComponentDimension = 2314
property_P31_hasQuantifiableComponentType = 2315
property_P76_isQuantifiableQualityOf = 2316
property_P77_isInvolvementIn = 2317
property_P78_hasInvolvementType = 2318
property_P79_isInvolvementOf = 2319
property_P80_isLinkedTo = 2320
property_P81_hasLinkType = 2321
property_P82_classifies = 2324
property_P83_classifiesWith = 2325
property_P65_hasParticipationRelationType = 2368
property_P66_isParticipationRelationOf = 2369
property_P67_hasParticipationRelationRole = 2370
property_P68_hasRoleQuality = 2371
property_P31_hasMentioningContent = 2415
property_P69_isDefinedInTheContextOf = 2416
property_P70_isEmbodiedIn = 2436
property_P71_hasPoliticalOrAdministrativeEntityType = 2437