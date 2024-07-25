from typing import List

class OntoObject:
    def __init__(self, pk: int, label: str, id: str):
        self.pk = pk
        self.label = label
        self.id = id

class Ontology:
    classes: List[OntoObject] = []
    properties: List[OntoObject] = []

    def __init__(self): 
        pass

    def klass(self, input: int | str) -> OntoObject:
        return self.__find(self.classes, input, 'class')

    def property(self, input: int | str) -> OntoObject:
        return self.__find(self.properties, input, 'property')

    def __find(self, ontoobjects: List[OntoObject], input: int | str, name=str) -> OntoObject:
        if isinstance(input, int): selection = [obj for obj in ontoobjects if input == obj.pk]
        elif isinstance(input, str): selection = [obj for obj in ontoobjects if input.lower() == obj.label.lower() or input.lower() == obj.id.lower()]

        if len(selection) == 0: raise Exception(f'Unknown ' + name + ' "' + input + '"')
        elif len(selection) == 1: return selection[0]
        else: raise Exception('Multiple ' + name + ' found with "' + input + '"')

ontology = Ontology()
ontology.classes.append(OntoObject(7, "Activity", "E7"))
ontology.classes.append(OntoObject(21, "Person", "E21"))
ontology.classes.append(OntoObject(340, "Physical Thing Life", "C19"))
ontology.classes.append(OntoObject(364, "Geographical Place Type", "C14"))
ontology.classes.append(OntoObject(5, "Event", "E5"))
ontology.classes.append(OntoObject(53, "Type", "E55"))
ontology.classes.append(OntoObject(60, "Formation", "E66"))
ontology.classes.append(OntoObject(62, "Dissolution", "E68"))
ontology.classes.append(OntoObject(63, "Death", "E69"))
ontology.classes.append(OntoObject(68, "Group", "E74"))
ontology.classes.append(OntoObject(78, "Joining", "E85"))
ontology.classes.append(OntoObject(79, "Leaving", "E86"))
ontology.classes.append(OntoObject(212, "Epistemic Location of a Physical Thing", "C15"))
ontology.classes.append(OntoObject(218, "Expression", "F2"))
ontology.classes.append(OntoObject(220, "Manifestation Singleton", "F4"))
ontology.classes.append(OntoObject(244, "Expression Creation", "F28"))
ontology.classes.append(OntoObject(332, "Activity Type", "C3"))
ontology.classes.append(OntoObject(363, "Geographical Place", "C13"))
ontology.classes.append(OntoObject(441, "Construction", "C17"))
ontology.classes.append(OntoObject(442, "Membership", "C5"))
ontology.classes.append(OntoObject(443, "Construction Type", "C18"))
ontology.classes.append(OntoObject(444, "Actor's Social Quality", "C2"))
ontology.classes.append(OntoObject(449, "Epistemic Location Type", "C16"))
ontology.classes.append(OntoObject(451, "Group Type", "C9"))
ontology.classes.append(OntoObject(608, "Membership Type", "C6"))
ontology.classes.append(OntoObject(717, "Monetary amount", "C21"))
ontology.classes.append(OntoObject(718, "Currency", "C22"))
ontology.classes.append(OntoObject(838, "Event Type", "C34"))
ontology.classes.append(OntoObject(839, "Location Reason", "C35"))
ontology.classes.append(OntoObject(969, "Relative Location of a Physical Thing", "C41"))
ontology.classes.append(OntoObject(1, "CRM Entity", "E1"))
ontology.classes.append(OntoObject(2, "Temporal Entity", "E2"))
ontology.classes.append(OntoObject(32, "Linguistic Object", "E33"))
ontology.classes.append(OntoObject(40, "Appellation", "E41"))
ontology.classes.append(OntoObject(41, "Identifier", "E42"))
ontology.classes.append(OntoObject(50, "Time-Span", "E52"))
ontology.classes.append(OntoObject(51, "Place", "E53"))
ontology.classes.append(OntoObject(54, "Language", "E56"))
ontology.classes.append(OntoObject(71, "Curated Holding", "E78"))
ontology.classes.append(OntoObject(84, "Presence", "E93"))
ontology.classes.append(OntoObject(219, "Manifestation Product Type", "F3"))
ontology.classes.append(OntoObject(221, "Item", "F5"))
ontology.classes.append(OntoObject(234, "Serial Work", "F18"))
ontology.classes.append(OntoObject(335, "Time Primitive", "E61"))
ontology.classes.append(OntoObject(338, "Number", "E60"))
ontology.classes.append(OntoObject(339, "String", "E62"))
ontology.classes.append(OntoObject(365, "Appellation in a Language", "C11"))
ontology.classes.append(OntoObject(445, "Argument", "C12"))
ontology.classes.append(OntoObject(450, "Manifestation Singleton Type", "C10"))
ontology.classes.append(OntoObject(452, "Type of manifestation product type", "C8"))
ontology.classes.append(OntoObject(454, "Expression Type", "C6"))
ontology.classes.append(OntoObject(455, "[Geovistory] Digital", "C1"))
ontology.classes.append(OntoObject(456, "Chunk", "C2"))
ontology.classes.append(OntoObject(457, "Spot", "C3"))
ontology.classes.append(OntoObject(459, "Argument's method", "C13"))
ontology.classes.append(OntoObject(502, "Web Request", "C4"))
ontology.classes.append(OntoObject(503, "Expression Portion", "C2"))
ontology.classes.append(OntoObject(516, "Expression Portion Type", "C3"))
ontology.classes.append(OntoObject(518, "Expression fragment", "C6"))
ontology.classes.append(OntoObject(519, "Item Type", "C5"))
ontology.classes.append(OntoObject(520, "Entity Quality Type", "C20"))
ontology.classes.append(OntoObject(521, "Cell", "C7"))
ontology.classes.append(OntoObject(607, "Web request type", "C8"))
ontology.classes.append(OntoObject(630, "Appellation in a Language Type", "C12"))
ontology.classes.append(OntoObject(635, "Tag", "C9"))
ontology.classes.append(OntoObject(657, "Reference", "C11"))
ontology.classes.append(OntoObject(689, "Duration", "C1"))
ontology.classes.append(OntoObject(690, "Time unit", "C2"))
ontology.classes.append(OntoObject(698, "Actor's Social Role", "C12"))
ontology.classes.append(OntoObject(707, "Numeric dimension", "C11"))
ontology.classes.append(OntoObject(708, "Numeric dimension type", "C12"))
ontology.classes.append(OntoObject(783, "Uniform Resource Locator (URL)", "C14"))
ontology.classes.append(OntoObject(784, "Short title", "C15"))
ontology.classes.append(OntoObject(785, "Text", "C16"))
ontology.classes.append(OntoObject(827, "Identifier Type", "C24"))
ontology.classes.append(OntoObject(867, "Asserted Actor's Role", "C9"))
ontology.classes.append(OntoObject(868, "Person Appellation in a Language", "C38"))
ontology.classes.append(OntoObject(869, "Person Appellation in a Language Type", "C39"))
ontology.classes.append(OntoObject(870, "Bibliographic Citation", "C10"))
ontology.classes.append(OntoObject(871, "Citation Style", "C11"))
ontology.classes.append(OntoObject(872, "Belonging to a Physical Collection", "C27"))
ontology.classes.append(OntoObject(873, "Collection Type", "C26"))
ontology.classes.append(OntoObject(874, "Manifestation Singleton Appellation Type", "C17"))
ontology.classes.append(OntoObject(967, "Uniform Resource Identifier (URI)", "C30"))
ontology.classes.append(OntoObject(1076, "Geographical Place Classification", "C48"))
ontology.classes.append(OntoObject(1210, "Geographical Place Kind", "C51"))
ontology.classes.append(OntoObject(118, "Naissance", "TyIn14"))
ontology.classes.append(OntoObject(128, "Décès", "TyIn26"))
ontology.classes.append(OntoObject(134, "Localisation", "TyIn36"))
ontology.classes.append(OntoObject(181, "Obtenir une qualité", "TyIn11"))
ontology.classes.append(OntoObject(189, "Passage d'un examen", "TyIn145"))
ontology.classes.append(OntoObject(191, "Suspension d'activité", "TyIn149"))
ontology.classes.append(OntoObject(196, "Création d'un acteur collectif", "TyIn30"))
ontology.classes.append(OntoObject(522, "Ship", "C2"))
ontology.classes.append(OntoObject(523, "Ship Voyage", "C1"))
ontology.classes.append(OntoObject(524, "Ship Type", "C3"))
ontology.classes.append(OntoObject(525, "Shipyard", "C4"))
ontology.classes.append(OntoObject(526, "Economic good", "C5"))
ontology.classes.append(OntoObject(527, "Transport", "C6"))
ontology.classes.append(OntoObject(528, "Stopover", "C7"))
ontology.classes.append(OntoObject(529, "VOC Chamber", "C8"))
ontology.classes.append(OntoObject(533, "Shipbuilding", "C12"))
ontology.classes.append(OntoObject(535, "Participation", "C15"))
ontology.classes.append(OntoObject(3, "Condition State", "E3"))
ontology.classes.append(OntoObject(18, "Physical Thing", "E18"))
ontology.classes.append(OntoObject(28, "Design or Procedure", "E29"))
ontology.classes.append(OntoObject(30, "Document", "E31"))
ontology.classes.append(OntoObject(34, "Title", "E35"))
ontology.classes.append(OntoObject(38, "Actor", "E39"))
ontology.classes.append(OntoObject(61, "Birth", "E67"))
ontology.classes.append(OntoObject(64, "Thing", "E70"))
ontology.classes.append(OntoObject(75, "Actor Appellation", "E82"))
ontology.classes.append(OntoObject(81, "Propositional Object", "E89"))
ontology.classes.append(OntoObject(556, "Outcomes (external processes)", "REO12"))
ontology.classes.append(OntoObject(557, "Disposition", "REO2"))
ontology.classes.append(OntoObject(558, "Position", "REO13"))
ontology.classes.append(OntoObject(559, "Environment", "REO3"))
ontology.classes.append(OntoObject(560, "Location", "REO9"))
ontology.classes.append(OntoObject(561, "Lighting", "REO8"))
ontology.classes.append(OntoObject(562, "Circumstances", "REO1"))
ontology.classes.append(OntoObject(563, "Intensity", "REO7"))
ontology.classes.append(OntoObject(564, "Frequency", "REO4"))
ontology.classes.append(OntoObject(565, "Nationality", "REO10"))
ontology.classes.append(OntoObject(566, "Gender", "REO5"))
ontology.classes.append(OntoObject(567, "Occupation", "REO11"))
ontology.classes.append(OntoObject(568, "Religion (temporal entity)", "REO15"))
ontology.classes.append(OntoObject(569, "Genre", "REO6"))
ontology.classes.append(OntoObject(570, "Provenance", "REO14"))
ontology.classes.append(OntoObject(571, "Status", "REO16"))
ontology.classes.append(OntoObject(629, "Gender", "C11"))
ontology.classes.append(OntoObject(636, "Occupation", "C7"))
ontology.classes.append(OntoObject(637, "Occupation (Temporal entity)", "C8"))
ontology.classes.append(OntoObject(642, "Habit", "REO17"))
ontology.classes.append(OntoObject(643, "Aim", "REO18"))
ontology.classes.append(OntoObject(644, "Skill", "REO19"))
ontology.classes.append(OntoObject(645, "Understanding", "REO20"))
ontology.classes.append(OntoObject(646, "Emotions", "REO21"))
ontology.classes.append(OntoObject(647, "Evaluation", "REO22"))
ontology.classes.append(OntoObject(648, "Effects (internal processes)", "REO23"))
ontology.classes.append(OntoObject(719, "Skill", "C21"))
ontology.classes.append(OntoObject(755, "Summary", "REO26"))
ontology.classes.append(OntoObject(789, "Mental imagery", "REO27"))
ontology.classes.append(OntoObject(790, "Memories (textual)", "REO28"))
ontology.classes.append(OntoObject(791, "Memories (non textual)", "REO29"))
ontology.classes.append(OntoObject(792, "Expectations", "REO30"))
ontology.classes.append(OntoObject(793, "Action", "REO31"))
ontology.classes.append(OntoObject(794, "Change in thinking", "REO32"))
ontology.classes.append(OntoObject(795, "Output", "REO33"))
ontology.classes.append(OntoObject(797, "Age (temporal entity)", "REO35"))
ontology.classes.append(OntoObject(798, "Citizenship", "REO36"))
ontology.classes.append(OntoObject(799, "Linguistic communities", "REO37"))
ontology.classes.append(OntoObject(800, "Ethnic communities", "REO38"))
ontology.classes.append(OntoObject(801, "Educational level", "REO39"))
ontology.classes.append(OntoObject(802, "Subject matter", "REO40"))
ontology.classes.append(OntoObject(803, "Medium", "REO41"))
ontology.classes.append(OntoObject(4, "Period", "E4"))
ontology.classes.append(OntoObject(6, "Destruction", "E6"))
ontology.classes.append(OntoObject(8, "Acquisition", "E8"))
ontology.classes.append(OntoObject(9, "Move", "E9"))
ontology.classes.append(OntoObject(10, "Transfer of Custody", "E10"))
ontology.classes.append(OntoObject(11, "Modification", "E11"))
ontology.classes.append(OntoObject(12, "Production", "E12"))
ontology.classes.append(OntoObject(13, "Attribute Assignment", "E13"))
ontology.classes.append(OntoObject(14, "Condition Assessment", "E14"))
ontology.classes.append(OntoObject(15, "Identifier Assignment", "E15"))
ontology.classes.append(OntoObject(16, "Measurement", "E16"))
ontology.classes.append(OntoObject(17, "Type Assignment", "E17"))
ontology.classes.append(OntoObject(19, "Physical Object", "E19"))
ontology.classes.append(OntoObject(22, "Human-Made Object", "E22"))
ontology.classes.append(OntoObject(23, "Physical Human-Made Thing", "E24"))
ontology.classes.append(OntoObject(25, "Physical Feature", "E26"))
ontology.classes.append(OntoObject(26, "Site", "E27"))
ontology.classes.append(OntoObject(27, "Conceptual Object", "E28"))
ontology.classes.append(OntoObject(29, "Right", "E30"))
ontology.classes.append(OntoObject(31, "Authority Document", "E32"))
ontology.classes.append(OntoObject(33, "Inscription", "E34"))
ontology.classes.append(OntoObject(35, "Visual Item", "E36"))
ontology.classes.append(OntoObject(36, "Mark", "E37"))
ontology.classes.append(OntoObject(37, "Image", "E38"))
ontology.classes.append(OntoObject(39, "Legal Body", "E40"))
ontology.classes.append(OntoObject(42, "Place Appellation", "E44"))
ontology.classes.append(OntoObject(43, "Address", "E45"))
ontology.classes.append(OntoObject(44, "Section Definition", "E46"))
ontology.classes.append(OntoObject(46, "Place Name", "E48"))
ontology.classes.append(OntoObject(47, "Time Appellation", "E49"))
ontology.classes.append(OntoObject(48, "Date", "E50"))
ontology.classes.append(OntoObject(49, "Contact Point", "E51"))
ontology.classes.append(OntoObject(52, "Dimension", "E54"))
ontology.classes.append(OntoObject(55, "Material", "E57"))
ontology.classes.append(OntoObject(56, "Measurement Unit", "E58"))
ontology.classes.append(OntoObject(59, "Creation", "E65"))
ontology.classes.append(OntoObject(65, "Human-Made Thing", "E71"))
ontology.classes.append(OntoObject(67, "Information Object", "E73"))
ontology.classes.append(OntoObject(69, "Conceptual Object Appellation", "E75"))
ontology.classes.append(OntoObject(70, "Persistent Item", "E77"))
ontology.classes.append(OntoObject(72, "Part Addition", "E79"))
ontology.classes.append(OntoObject(73, "Part Removal", "E80"))
ontology.classes.append(OntoObject(74, "Transformation", "E81"))
ontology.classes.append(OntoObject(76, "Type Creation", "E83"))
ontology.classes.append(OntoObject(80, "Curation Activity", "E87"))
ontology.classes.append(OntoObject(82, "Symbolic Object", "E90"))
ontology.classes.append(OntoObject(83, "Spacetime Volume", "E92"))
ontology.classes.append(OntoObject(211, "Entity Quality", "C1"))
ontology.classes.append(OntoObject(471, "Belief", "I2"))
ontology.classes.append(OntoObject(472, "Inference Logic", "I3"))
ontology.classes.append(OntoObject(473, "Proposition Set", "I4"))
ontology.classes.append(OntoObject(474, "Inference Making", "I5"))
ontology.classes.append(OntoObject(475, "Belief Value", "I6"))
ontology.classes.append(OntoObject(572, "Weaving", "T1"))
ontology.classes.append(OntoObject(573, "Entering (Deprecated)", "T2"))
ontology.classes.append(OntoObject(574, "Spinning (deprecated)", "T3"))
ontology.classes.append(OntoObject(575, "Throwing (deprecated)", "T4"))
ontology.classes.append(OntoObject(576, "Warping (deprecated)", "T5"))
ontology.classes.append(OntoObject(577, "Loom", "T6"))
ontology.classes.append(OntoObject(578, "Fabric", "T7"))
ontology.classes.append(OntoObject(579, "Part Weaving", "T8"))
ontology.classes.append(OntoObject(580, "Pattern Zone", "T9"))
ontology.classes.append(OntoObject(581, "Ground", "T10"))
ontology.classes.append(OntoObject(582, "Style", "T11"))
ontology.classes.append(OntoObject(583, "Selvedge (deprecated)", "T12"))
ontology.classes.append(OntoObject(584, "Style Assignment", "T13"))
ontology.classes.append(OntoObject(585, "Starting Border (deprecated)", "T14"))
ontology.classes.append(OntoObject(586, "Yarn", "T15"))
ontology.classes.append(OntoObject(587, "Warp", "T16"))
ontology.classes.append(OntoObject(588, "Weft", "T17"))
ontology.classes.append(OntoObject(589, "Motif", "T18"))
ontology.classes.append(OntoObject(590, "Object Domain Assignment", "T19"))
ontology.classes.append(OntoObject(591, "Twist", "T20"))
ontology.classes.append(OntoObject(592, "Weave", "T21"))
ontology.classes.append(OntoObject(594, "Fabric Type", "T23"))
ontology.classes.append(OntoObject(595, "Pattern Unit", "T24"))
ontology.classes.append(OntoObject(596, "Weaving Technique", "T25"))
ontology.classes.append(OntoObject(597, "Loom Type", "T26"))
ontology.classes.append(OntoObject(599, "Yarn Type", "T28"))
ontology.classes.append(OntoObject(600, "Twist Type", "T29"))
ontology.classes.append(OntoObject(601, "Warp Type", "T30"))
ontology.classes.append(OntoObject(602, "Warping Type (deprecated)", "T31"))
ontology.classes.append(OntoObject(603, "Weave Type", "T32"))
ontology.classes.append(OntoObject(604, "Weft Type", "T33"))
ontology.classes.append(OntoObject(605, "Motif Type", "T34"))
ontology.classes.append(OntoObject(606, "Object Type Assignment", "T35"))
ontology.classes.append(OntoObject(760, "Quantifiable Quality", "C28"))
ontology.classes.append(OntoObject(832, "Embroidery", "T36"))
ontology.classes.append(OntoObject(833, "Galloon", "T37"))
ontology.classes.append(OntoObject(834, "Lining", "T38"))
ontology.classes.append(OntoObject(633, "Relationship", "C9"))
ontology.classes.append(OntoObject(634, "Type of Persons' Interaction", "C10"))
ontology.classes.append(OntoObject(702, "Persons' Interaction", "C18"))
ontology.classes.append(OntoObject(808, "Legal Location of an Actor", "C28"))
ontology.classes.append(OntoObject(883, "Legal Location Type", "C33"))
ontology.classes.append(OntoObject(384, "Encounter Event", "S19"))
ontology.classes.append(OntoObject(727, "Use", "C23"))
ontology.classes.append(OntoObject(728, "Use type", "C24"))
ontology.classes.append(OntoObject(894, "Physical Man-Made Thing Type", "C2"))
ontology.classes.append(OntoObject(213, "Social Perception of an Actor", "C1"))
ontology.classes.append(OntoObject(631, "Pre-matrimonial enquiry", "C1"))
ontology.classes.append(OntoObject(638, "Marital status", "C2"))
ontology.classes.append(OntoObject(664, "Pre-matrimonial enquiry motivation type", "C3"))
ontology.classes.append(OntoObject(691, "Account of a journey or stay", "C4"))
ontology.classes.append(OntoObject(694, "Concept referred to in a journey's or stay's account", "C5"))
ontology.classes.append(OntoObject(695, "Frequency class", "C6"))
ontology.classes.append(OntoObject(334, "Social Relationship", "C3"))
ontology.classes.append(OntoObject(632, "Social Relationship Type", "C4"))
ontology.classes.append(OntoObject(1714, "Actor's Role in a Social Relationship", "C43"))
ontology.classes.append(OntoObject(897, "Activity Domain", "C34"))
ontology.classes.append(OntoObject(677, "Physical Human-Made Thing Type", "C4"))
ontology.classes.append(OntoObject(709, "Length", "C13"))
ontology.classes.append(OntoObject(710, "Length measurement unit", "C14"))
ontology.classes.append(OntoObject(711, "Weight", "C15"))
ontology.classes.append(OntoObject(712, "Weight measurement unit", "C16"))
ontology.classes.append(OntoObject(713, "Area", "C17"))
ontology.classes.append(OntoObject(714, "Area measurement unit", "C18"))
ontology.classes.append(OntoObject(715, "Volume measurement unit", "C19"))
ontology.classes.append(OntoObject(716, "Volume", "C20"))
ontology.classes.append(OntoObject(726, "Physical Component", "C22"))
ontology.classes.append(OntoObject(217, "Work", "F1"))
ontology.classes.append(OntoObject(676, "Expression Publication Event", "C1"))
ontology.classes.append(OntoObject(721, "Procedure", "C4"))
ontology.classes.append(OntoObject(722, "Step", "C5"))
ontology.classes.append(OntoObject(723, "Component of a Recipe", "C6"))
ontology.classes.append(OntoObject(724, "Procedure Type", "C7"))
ontology.classes.append(OntoObject(725, "Step Type", "C8"))
ontology.classes.append(OntoObject(1290, "General Technique", "C53"))
ontology.classes.append(OntoObject(1752, "Expression Portion Classification", "C18"))
ontology.classes.append(OntoObject(1756, "Subject", "C19"))
ontology.classes.append(OntoObject(688, "Holding of a Right or Obligation", "C14"))
ontology.classes.append(OntoObject(697, "Social Role Embodiment", "C13"))
ontology.classes.append(OntoObject(701, "Custom or Law", "C17"))
ontology.classes.append(OntoObject(720, "Legal Quality Type", "C22"))
ontology.classes.append(OntoObject(758, "Religious Identity", "C23"))
ontology.classes.append(OntoObject(759, "Religion or Religious Denomination", "C24"))
ontology.classes.append(OntoObject(786, "Abstract individual", "C32"))
ontology.classes.append(OntoObject(787, "Political or Administrative Entity", "C25"))
ontology.classes.append(OntoObject(806, "Legal Quality", "C26"))
ontology.classes.append(OntoObject(807, "Legal Fact", "C27"))
ontology.classes.append(OntoObject(847, "Legal Quality Acquisition", "C29"))
ontology.classes.append(OntoObject(848, "Actor's Legal Quality Acquisition Type", "C30"))
ontology.classes.append(OntoObject(866, "Holding of a Right Type", "C31"))
ontology.classes.append(OntoObject(882, "Social Role Type", "C32"))
ontology.classes.append(OntoObject(887, "Intentional Event", "C10"))
ontology.classes.append(OntoObject(1491, "Political or Administrative Entity Type", "C42"))
ontology.classes.append(OntoObject(704, "Being in Force", "C20"))
ontology.classes.append(OntoObject(705, "Custom or Law Type", "C21"))
ontology.classes.append(OntoObject(656, "Namespace", "C10"))
ontology.classes.append(OntoObject(826, "Identification", "C23"))
ontology.classes.append(OntoObject(388, "Excavation Process Unit", "A1"))
ontology.classes.append(OntoObject(389, "Stratigraphic Volume Unit", "A2"))
ontology.classes.append(OntoObject(390, "Stratigraphic Interface", "A3"))
ontology.classes.append(OntoObject(394, "Embedding", "A7"))
ontology.classes.append(OntoObject(396, "Archaeological Excavation", "A9"))
ontology.classes.append(OntoObject(840, "Archaeological Excavation Type", "C1"))
ontology.classes.append(OntoObject(841, "Excavation Process Unit Type", "C2"))
ontology.classes.append(OntoObject(680, "Built Work", "B1"))
ontology.classes.append(OntoObject(681, "Morphological Building Section", "B2"))
ontology.classes.append(OntoObject(682, "Filled Morphological Building Section", "B3"))
ontology.classes.append(OntoObject(683, "Empty Morphological Building Section", "B4"))
ontology.classes.append(OntoObject(947, "Dimension Kind", "C27"))
ontology.classes.append(OntoObject(831, "Teaching", "C1"))
ontology.classes.append(OntoObject(859, "Academic Discipline", "C5"))
ontology.classes.append(OntoObject(860, "Academic Chair", "C6"))
ontology.classes.append(OntoObject(861, "Academic Position", "C7"))
ontology.classes.append(OntoObject(846, "Study", "C2"))
ontology.classes.append(OntoObject(849, "Obtaining a Study Title", "C3"))
ontology.classes.append(OntoObject(850, "Study title", "C4"))
ontology.classes.append(OntoObject(1766, "Group Classification", "C70"))
ontology.classes.append(OntoObject(879, "Taking Care of a Person", "C1"))
ontology.classes.append(OntoObject(880, "Attending a School", "C2"))
ontology.classes.append(OntoObject(884, "Taking Care of a Person Type", "C3"))
ontology.classes.append(OntoObject(885, "Attending a School Type", "C4"))
ontology.classes.append(OntoObject(946, "Actor's Quality in Relation to an Event", "C35"))
ontology.classes.append(OntoObject(898, "Table", "C18"))
ontology.classes.append(OntoObject(899, "Definition", "C19"))
ontology.classes.append(OntoObject(900, "Comment", "C20"))
ontology.classes.append(OntoObject(903, "Text type", "C23"))
ontology.classes.append(OntoObject(904, "Comment type", "C24"))
ontology.classes.append(OntoObject(933, "Annotation in Text", "C26"))
ontology.classes.append(OntoObject(934, "Annotation in Table", "C27"))
ontology.classes.append(OntoObject(935, "Mentioning", "C28"))
ontology.classes.append(OntoObject(936, "Table Value", "C29"))
ontology.classes.append(OntoObject(968, "Mentioning in Table", "C31"))
ontology.classes.append(OntoObject(1150, "Propositional Datation", "C13"))
ontology.classes.append(OntoObject(1295, "Datation Type", "C14"))
ontology.classes.append(OntoObject(627, "Building", "Building"))
ontology.classes.append(OntoObject(809, "A1_Endurant", "A1_Endurant"))
ontology.classes.append(OntoObject(810, "A3_Quality", "A3_Quality"))
ontology.classes.append(OntoObject(811, "A2_Perdurant", "A2_Perdurant"))
ontology.classes.append(OntoObject(916, "A22111_A-Procedure", "A22111_A-Procedure"))
ontology.classes.append(OntoObject(922, "A2224_End_of_activity", "A2224_End_of_activity"))
ontology.classes.append(OntoObject(923, "A2225_Patrimonalization", "A2225_Patrimonalization"))
ontology.classes.append(OntoObject(925, "A0_Any_Artefact_Entity", "A0_Any_Artefact_Entity"))
ontology.classes.append(OntoObject(930, "Glacière", "C9"))
ontology.classes.append(OntoObject(948, "Information Object Type", "C28"))
ontology.classes.append(OntoObject(955, "Dedication", "C12"))
ontology.classes.append(OntoObject(247, "Performance", "F31"))
ontology.classes.append(OntoObject(956, "Performance Type", "C29"))
ontology.classes.append(OntoObject(1063, "Move Type", "C31"))
ontology.classes.append(OntoObject(1065, "Actor's Movement or Journey", "C1"))
ontology.classes.append(OntoObject(1066, "Stopover", "C2"))
ontology.classes.append(OntoObject(1067, "Stopover Type", "C3"))
ontology.classes.append(OntoObject(1068, "Actor's Movement or Journey Type", "C4"))
ontology.classes.append(OntoObject(1069, "Carrier's Journey", "C5"))
ontology.classes.append(OntoObject(1070, "Carrier's Journey Type", "C6"))
ontology.classes.append(OntoObject(1071, "Actor's Coerced Trip", "C7"))
ontology.classes.append(OntoObject(1072, "Actor's Coerced Trip Type", "C8"))
ontology.classes.append(OntoObject(369, "Observation", "S4"))
ontology.classes.append(OntoObject(374, "Property Type", "S9"))
ontology.classes.append(OntoObject(1077, "Observed Entity Type", "C32"))
ontology.classes.append(OntoObject(971, "Relative Location Type", "C43"))
ontology.classes.append(OntoObject(1152, "Amount of Matter", "C49"))
ontology.classes.append(OntoObject(1289, "Physical Set", "C52"))
ontology.classes.append(OntoObject(752, "Intentional Collective", "C25"))
ontology.classes.append(OntoObject(881, "Intentional Entity", "C9"))
ontology.classes.append(OntoObject(1361, "Physical Human-Made Thing Classification", "C55"))
ontology.classes.append(OntoObject(1296, "Participation Type", "C36"))
ontology.classes.append(OntoObject(1373, "Planned Move", "C15"))
ontology.classes.append(OntoObject(1374, "Quantifiable Component", "C16"))
ontology.classes.append(OntoObject(1375, "Quantifiable Component Type", "C17"))
ontology.classes.append(OntoObject(696, "Epistemic Situation", "C3"))
ontology.classes.append(OntoObject(1371, "Epistemic Situation Type", "C56"))
ontology.classes.append(OntoObject(1377, "Quantifiable Quality of an Epistemic Situation", "C59"))
ontology.classes.append(OntoObject(1378, "Thing Involved in an Epistemic Situation", "C60"))
ontology.classes.append(OntoObject(1379, "Type of Involvement of a Thing in an Epistemic Situation", "C61"))
ontology.classes.append(OntoObject(1372, "Quantifiable Quality of a Spatio-Temporal Phenomenon", "C57"))
ontology.classes.append(OntoObject(1380, "Link", "C62"))
ontology.classes.append(OntoObject(1381, "Link Type", "C63"))
ontology.classes.append(OntoObject(1383, "Activity Purpose", "C34"))
ontology.classes.append(OntoObject(1384, "Event Classification", "C64"))
ontology.classes.append(OntoObject(1385, "Event Classification Type", "C65"))
ontology.classes.append(OntoObject(973, "Physical Displacement", "C45"))
ontology.classes.append(OntoObject(1431, "Participation Relation", "C39"))
ontology.classes.append(OntoObject(1432, "Participation Relation Type", "C40"))
ontology.classes.append(OntoObject(1433, "Role in Participation Relation", "C41"))
ontology.classes.append(OntoObject(1062, "Intentional Expression", "C46"))
ontology.classes.append(OntoObject(1064, "Intentional Expression Type", "C47"))
ontology.classes.append(OntoObject(1775, "Quantifiable Quality of an Intentional Event", "C71"))
ontology.classes.append(OntoObject(57, "Beginning of Existence", "E63"))
ontology.classes.append(OntoObject(58, "End of Existence", "E64"))
ontology.classes.append(OntoObject(336, "Space Primitive", "E94"))
ontology.classes.append(OntoObject(366, "Matter Removal", "S1"))
ontology.classes.append(OntoObject(375, "Material Substantial", "S10"))
ontology.classes.append(OntoObject(380, "Observable Entity", "S15"))
ontology.classes.append(OntoObject(1386, "Built Entity", "CP1"))
ontology.classes.append(OntoObject(1387, "Architecture work", "CP2"))
ontology.classes.append(OntoObject(1388, "Construction Unit", "CP3"))
ontology.classes.append(OntoObject(1389, "Construction Component", "CP4"))
ontology.classes.append(OntoObject(1390, "Construction Element Plural", "CP5"))
ontology.classes.append(OntoObject(1391, "Construction Element Singular", "CP6"))
ontology.classes.append(OntoObject(1392, "Architecture Decoration", "CP7"))
ontology.classes.append(OntoObject(1393, "Equipment", "CP8"))
ontology.classes.append(OntoObject(1394, "Building Material", "CP9"))
ontology.classes.append(OntoObject(1395, "Building Unit", "CP10"))
ontology.classes.append(OntoObject(1396, "Building Front", "CP11"))
ontology.classes.append(OntoObject(1397, "Building Floor", "CP12"))
ontology.classes.append(OntoObject(1398, "Urban Unit", "CP13"))
ontology.classes.append(OntoObject(1401, "Urban Unit Front", "CP14"))
ontology.classes.append(OntoObject(1402, "Open Air Area", "CP15"))
ontology.classes.append(OntoObject(1403, "Urban Area", "CP16"))
ontology.classes.append(OntoObject(1404, "Cultural Heritage Landscape Element", "CP17"))
ontology.classes.append(OntoObject(1405, "Space Entity", "CP18"))
ontology.classes.append(OntoObject(1406, "Historic Centre", "CP19"))
ontology.classes.append(OntoObject(1407, "Construction Work", "CP20"))
ontology.classes.append(OntoObject(1408, "Space Unit", "CP21"))
ontology.classes.append(OntoObject(1409, "Space Component", "CP22"))
ontology.classes.append(OntoObject(1410, "Maintenance", "CP23"))
ontology.classes.append(OntoObject(1411, "Architecture Conservation Project Activity", "CP24"))
ontology.classes.append(OntoObject(1412, "Conservation Intervention", "CP25"))
ontology.classes.append(OntoObject(1413, "Typological Variation", "CP26"))
ontology.classes.append(OntoObject(1414, "Architecture Analysis Output", "CP27"))
ontology.classes.append(OntoObject(1415, "Building Feature", "CP28"))
ontology.classes.append(OntoObject(1416, "Building Phase", "CP29"))
ontology.classes.append(OntoObject(1417, "Architecture Condition Assessment", "CP30"))
ontology.classes.append(OntoObject(1418, "Mechanical Damage Assessment", "CP31"))
ontology.classes.append(OntoObject(1419, "Architecture Features Analysis", "CP32"))
ontology.classes.append(OntoObject(1420, "Architecture Conservation Project", "CP33"))
ontology.classes.append(OntoObject(1421, "Architecture Depiction", "CP34"))
ontology.classes.append(OntoObject(1422, "Building-Formal Type", "CP35"))
ontology.classes.append(OntoObject(1423, "Architecture Type", "CP36"))
ontology.classes.append(OntoObject(1424, "Architecture Graphic Representation Type", "CP37"))
ontology.classes.append(OntoObject(1425, "Architecture Representation Object", "CP38"))
ontology.classes.append(OntoObject(1426, "Architecture Alpha-Numeric Representation Type", "CP39"))
ontology.classes.append(OntoObject(1427, "Historic Centre", "CP40"))
ontology.classes.append(OntoObject(1703, "Environmental Observable Entity", "CP41"))
ontology.classes.append(OntoObject(1704, "Construction Site", "CP44"))
ontology.classes.append(OntoObject(1705, "Material Decay", "CP42"))
ontology.classes.append(OntoObject(1706, "Structural Damage", "CP43"))
ontology.classes.append(OntoObject(1707, "Architecture Project", "CP45"))
ontology.classes.append(OntoObject(1708, "Building Activity", "CP46"))
ontology.classes.append(OntoObject(1715, "Urban Plan", "CP49"))
ontology.classes.append(OntoObject(1753, "Animal", "C67"))
ontology.classes.append(OntoObject(1754, "Biological Object Classification Type", "C68"))
ontology.classes.append(OntoObject(1768, "Propositional Object Type", "C35"))

class PkClass:
   E7_activity = 7
   E21_person = 21
   C19_physicalThingLife = 340
   C14_geographicalPlaceType = 364
   E5_event = 5
   E55_type = 53
   E66_formation = 60
   E68_dissolution = 62
   E69_death = 63
   E74_group = 68
   E85_joining = 78
   E86_leaving = 79
   C15_epistemicLocationOfAPhysicalThing = 212
   F2_expression = 218
   F4_manifestationSingleton = 220
   F28_expressionCreation = 244
   C3_activityType = 332
   C13_geographicalPlace = 363
   C17_construction = 441
   C5_membership = 442
   C18_constructionType = 443
   C2_actorSSocialQuality = 444
   C16_epistemicLocationType = 449
   C9_groupType = 451
   C6_membershipType = 608
   C21_monetaryAmount = 717
   C22_currency = 718
   C34_eventType = 838
   C35_locationReason = 839
   C41_relativeLocationOfAPhysicalThing = 969
   E1_crmEntity = 1
   E2_temporalEntity = 2
   E33_linguisticObject = 32
   E41_appellation = 40
   E42_identifier = 41
   E52_timeSpan = 50
   E53_place = 51
   E56_language = 54
   E78_curatedHolding = 71
   E93_presence = 84
   F3_manifestationProductType = 219
   F5_item = 221
   F18_serialWork = 234
   E61_timePrimitive = 335
   E60_number = 338
   E62_string = 339
   C11_appellationInALanguage = 365
   C12_argument = 445
   C10_manifestationSingletonType = 450
   C8_typeOfManifestationProductType = 452
   C6_expressionType = 454
   C1_geovistoryDigital = 455
   C2_chunk = 456
   C3_spot = 457
   C13_argumentSMethod = 459
   C4_webRequest = 502
   C2_expressionPortion = 503
   C3_expressionPortionType = 516
   C6_expressionFragment = 518
   C5_itemType = 519
   C20_entityQualityType = 520
   C7_cell = 521
   C8_webRequestType = 607
   C12_appellationInALanguageType = 630
   C9_tag = 635
   C11_reference = 657
   C1_duration = 689
   C2_timeUnit = 690
   C12_actorSSocialRole = 698
   C11_numericDimension = 707
   C12_numericDimensionType = 708
   C14_uniformResourceLocatorUrl = 783
   C15_shortTitle = 784
   C16_text = 785
   C24_identifierType = 827
   C9_assertedActorSRole = 867
   C38_personAppellationInALanguage = 868
   C39_personAppellationInALanguageType = 869
   C10_bibliographicCitation = 870
   C11_citationStyle = 871
   C27_belongingToAPhysicalCollection = 872
   C26_collectionType = 873
   C17_manifestationSingletonAppellationType = 874
   C30_uniformResourceIdentifierUri = 967
   C48_geographicalPlaceClassification = 1076
   C51_geographicalPlaceKind = 1210
   TyIn14_naissance = 118
   TyIn26_décès = 128
   TyIn36_localisation = 134
   TyIn11_obtenirUneQualité = 181
   TyIn145_passageDUnExamen = 189
   TyIn149_suspensionDActivité = 191
   TyIn30_créationDUnActeurCollectif = 196
   C2_ship = 522
   C1_shipVoyage = 523
   C3_shipType = 524
   C4_shipyard = 525
   C5_economicGood = 526
   C6_transport = 527
   C7_stopover = 528
   C8_vocChamber = 529
   C12_shipbuilding = 533
   C15_participation = 535
   E3_conditionState = 3
   E18_physicalThing = 18
   E29_designOrProcedure = 28
   E31_document = 30
   E35_title = 34
   E39_actor = 38
   E67_birth = 61
   E70_thing = 64
   E82_actorAppellation = 75
   E89_propositionalObject = 81
   REO12_outcomesExternalProcesses = 556
   REO2_disposition = 557
   REO13_position = 558
   REO3_environment = 559
   REO9_location = 560
   REO8_lighting = 561
   REO1_circumstances = 562
   REO7_intensity = 563
   REO4_frequency = 564
   REO10_nationality = 565
   REO5_gender = 566
   REO11_occupation = 567
   REO15_religionTemporalEntity = 568
   REO6_genre = 569
   REO14_provenance = 570
   REO16_status = 571
   C11_gender = 629
   C7_occupation = 636
   C8_occupationTemporalEntity = 637
   REO17_habit = 642
   REO18_aim = 643
   REO19_skill = 644
   REO20_understanding = 645
   REO21_emotions = 646
   REO22_evaluation = 647
   REO23_effectsInternalProcesses = 648
   C21_skill = 719
   REO26_summary = 755
   REO27_mentalImagery = 789
   REO28_memoriesTextual = 790
   REO29_memoriesNonTextual = 791
   REO30_expectations = 792
   REO31_action = 793
   REO32_changeInThinking = 794
   REO33_output = 795
   REO35_ageTemporalEntity = 797
   REO36_citizenship = 798
   REO37_linguisticCommunities = 799
   REO38_ethnicCommunities = 800
   REO39_educationalLevel = 801
   REO40_subjectMatter = 802
   REO41_medium = 803
   E4_period = 4
   E6_destruction = 6
   E8_acquisition = 8
   E9_move = 9
   E10_transferOfCustody = 10
   E11_modification = 11
   E12_production = 12
   E13_attributeAssignment = 13
   E14_conditionAssessment = 14
   E15_identifierAssignment = 15
   E16_measurement = 16
   E17_typeAssignment = 17
   E19_physicalObject = 19
   E22_humanMadeObject = 22
   E24_physicalHumanMadeThing = 23
   E26_physicalFeature = 25
   E27_site = 26
   E28_conceptualObject = 27
   E30_right = 29
   E32_authorityDocument = 31
   E34_inscription = 33
   E36_visualItem = 35
   E37_mark = 36
   E38_image = 37
   E40_legalBody = 39
   E44_placeAppellation = 42
   E45_address = 43
   E46_sectionDefinition = 44
   E48_placeName = 46
   E49_timeAppellation = 47
   E50_date = 48
   E51_contactPoint = 49
   E54_dimension = 52
   E57_material = 55
   E58_measurementUnit = 56
   E65_creation = 59
   E71_humanMadeThing = 65
   E73_informationObject = 67
   E75_conceptualObjectAppellation = 69
   E77_persistentItem = 70
   E79_partAddition = 72
   E80_partRemoval = 73
   E81_transformation = 74
   E83_typeCreation = 76
   E87_curationActivity = 80
   E90_symbolicObject = 82
   E92_spacetimeVolume = 83
   C1_entityQuality = 211
   I2_belief = 471
   I3_inferenceLogic = 472
   I4_propositionSet = 473
   I5_inferenceMaking = 474
   I6_beliefValue = 475
   T1_weaving = 572
   T2_enteringDeprecated = 573
   T3_spinningDeprecated = 574
   T4_throwingDeprecated = 575
   T5_warpingDeprecated = 576
   T6_loom = 577
   T7_fabric = 578
   T8_partWeaving = 579
   T9_patternZone = 580
   T10_ground = 581
   T11_style = 582
   T12_selvedgeDeprecated = 583
   T13_styleAssignment = 584
   T14_startingBorderDeprecated = 585
   T15_yarn = 586
   T16_warp = 587
   T17_weft = 588
   T18_motif = 589
   T19_objectDomainAssignment = 590
   T20_twist = 591
   T21_weave = 592
   T23_fabricType = 594
   T24_patternUnit = 595
   T25_weavingTechnique = 596
   T26_loomType = 597
   T28_yarnType = 599
   T29_twistType = 600
   T30_warpType = 601
   T31_warpingTypeDeprecated = 602
   T32_weaveType = 603
   T33_weftType = 604
   T34_motifType = 605
   T35_objectTypeAssignment = 606
   C28_quantifiableQuality = 760
   T36_embroidery = 832
   T37_galloon = 833
   T38_lining = 834
   C9_relationship = 633
   C10_typeOfPersonsInteraction = 634
   C18_personsInteraction = 702
   C28_legalLocationOfAnActor = 808
   C33_legalLocationType = 883
   S19_encounterEvent = 384
   C23_use = 727
   C24_useType = 728
   C2_physicalManMadeThingType = 894
   C1_socialPerceptionOfAnActor = 213
   C1_preMatrimonialEnquiry = 631
   C2_maritalStatus = 638
   C3_preMatrimonialEnquiryMotivationType = 664
   C4_accountOfAJourneyOrStay = 691
   C5_conceptReferredToInAJourneySOrStaySAccount = 694
   C6_frequencyClass = 695
   C3_socialRelationship = 334
   C4_socialRelationshipType = 632
   C43_actorSRoleInASocialRelationship = 1714
   C34_activityDomain = 897
   C4_physicalHumanMadeThingType = 677
   C13_length = 709
   C14_lengthMeasurementUnit = 710
   C15_weight = 711
   C16_weightMeasurementUnit = 712
   C17_area = 713
   C18_areaMeasurementUnit = 714
   C19_volumeMeasurementUnit = 715
   C20_volume = 716
   C22_physicalComponent = 726
   F1_work = 217
   C1_expressionPublicationEvent = 676
   C4_procedure = 721
   C5_step = 722
   C6_componentOfARecipe = 723
   C7_procedureType = 724
   C8_stepType = 725
   C53_generalTechnique = 1290
   C18_expressionPortionClassification = 1752
   C19_subject = 1756
   C14_holdingOfARightOrObligation = 688
   C13_socialRoleEmbodiment = 697
   C17_customOrLaw = 701
   C22_legalQualityType = 720
   C23_religiousIdentity = 758
   C24_religionOrReligiousDenomination = 759
   C32_abstractIndividual = 786
   C25_politicalOrAdministrativeEntity = 787
   C26_legalQuality = 806
   C27_legalFact = 807
   C29_legalQualityAcquisition = 847
   C30_actorSLegalQualityAcquisitionType = 848
   C31_holdingOfARightType = 866
   C32_socialRoleType = 882
   C10_intentionalEvent = 887
   C42_politicalOrAdministrativeEntityType = 1491
   C20_beingInForce = 704
   C21_customOrLawType = 705
   C10_namespace = 656
   C23_identification = 826
   A1_excavationProcessUnit = 388
   A2_stratigraphicVolumeUnit = 389
   A3_stratigraphicInterface = 390
   A7_embedding = 394
   A9_archaeologicalExcavation = 396
   C1_archaeologicalExcavationType = 840
   C2_excavationProcessUnitType = 841
   B1_builtWork = 680
   B2_morphologicalBuildingSection = 681
   B3_filledMorphologicalBuildingSection = 682
   B4_emptyMorphologicalBuildingSection = 683
   C27_dimensionKind = 947
   C1_teaching = 831
   C5_academicDiscipline = 859
   C6_academicChair = 860
   C7_academicPosition = 861
   C2_study = 846
   C3_obtainingAStudyTitle = 849
   C4_studyTitle = 850
   C70_groupClassification = 1766
   C1_takingCareOfAPerson = 879
   C2_attendingASchool = 880
   C3_takingCareOfAPersonType = 884
   C4_attendingASchoolType = 885
   C35_actorSQualityInRelationToAnEvent = 946
   C18_table = 898
   C19_definition = 899
   C20_comment = 900
   C23_textType = 903
   C24_commentType = 904
   C26_annotationInText = 933
   C27_annotationInTable = 934
   C28_mentioning = 935
   C29_tableValue = 936
   C31_mentioningInTable = 968
   C13_propositionalDatation = 1150
   C14_datationType = 1295
   Building_building = 627
   A1_Endurant_a1Endurant = 809
   A3_Quality_a3Quality = 810
   A2_Perdurant_a2Perdurant = 811
   A22111_A_Procedure_a22111AProcedure = 916
   A2224_End_of_activity_a2224EndOfActivity = 922
   A2225_Patrimonalization_a2225Patrimonalization = 923
   A0_Any_Artefact_Entity_a0AnyArtefactEntity = 925
   C9_glacière = 930
   C28_informationObjectType = 948
   C12_dedication = 955
   F31_performance = 247
   C29_performanceType = 956
   C31_moveType = 1063
   C1_actorSMovementOrJourney = 1065
   C2_stopover = 1066
   C3_stopoverType = 1067
   C4_actorSMovementOrJourneyType = 1068
   C5_carrierSJourney = 1069
   C6_carrierSJourneyType = 1070
   C7_actorSCoercedTrip = 1071
   C8_actorSCoercedTripType = 1072
   S4_observation = 369
   S9_propertyType = 374
   C32_observedEntityType = 1077
   C43_relativeLocationType = 971
   C49_amountOfMatter = 1152
   C52_physicalSet = 1289
   C25_intentionalCollective = 752
   C9_intentionalEntity = 881
   C55_physicalHumanMadeThingClassification = 1361
   C36_participationType = 1296
   C15_plannedMove = 1373
   C16_quantifiableComponent = 1374
   C17_quantifiableComponentType = 1375
   C3_epistemicSituation = 696
   C56_epistemicSituationType = 1371
   C59_quantifiableQualityOfAnEpistemicSituation = 1377
   C60_thingInvolvedInAnEpistemicSituation = 1378
   C61_typeOfInvolvementOfAThingInAnEpistemicSituation = 1379
   C57_quantifiableQualityOfASpatioTemporalPhenomenon = 1372
   C62_link = 1380
   C63_linkType = 1381
   C34_activityPurpose = 1383
   C64_eventClassification = 1384
   C65_eventClassificationType = 1385
   C45_physicalDisplacement = 973
   C39_participationRelation = 1431
   C40_participationRelationType = 1432
   C41_roleInParticipationRelation = 1433
   C46_intentionalExpression = 1062
   C47_intentionalExpressionType = 1064
   C71_quantifiableQualityOfAnIntentionalEvent = 1775
   E63_beginningOfExistence = 57
   E64_endOfExistence = 58
   E94_spacePrimitive = 336
   S1_matterRemoval = 366
   S10_materialSubstantial = 375
   S15_observableEntity = 380
   CP1_builtEntity = 1386
   CP2_architectureWork = 1387
   CP3_constructionUnit = 1388
   CP4_constructionComponent = 1389
   CP5_constructionElementPlural = 1390
   CP6_constructionElementSingular = 1391
   CP7_architectureDecoration = 1392
   CP8_equipment = 1393
   CP9_buildingMaterial = 1394
   CP10_buildingUnit = 1395
   CP11_buildingFront = 1396
   CP12_buildingFloor = 1397
   CP13_urbanUnit = 1398
   CP14_urbanUnitFront = 1401
   CP15_openAirArea = 1402
   CP16_urbanArea = 1403
   CP17_culturalHeritageLandscapeElement = 1404
   CP18_spaceEntity = 1405
   CP19_historicCentre = 1406
   CP20_constructionWork = 1407
   CP21_spaceUnit = 1408
   CP22_spaceComponent = 1409
   CP23_maintenance = 1410
   CP24_architectureConservationProjectActivity = 1411
   CP25_conservationIntervention = 1412
   CP26_typologicalVariation = 1413
   CP27_architectureAnalysisOutput = 1414
   CP28_buildingFeature = 1415
   CP29_buildingPhase = 1416
   CP30_architectureConditionAssessment = 1417
   CP31_mechanicalDamageAssessment = 1418
   CP32_architectureFeaturesAnalysis = 1419
   CP33_architectureConservationProject = 1420
   CP34_architectureDepiction = 1421
   CP35_buildingFormalType = 1422
   CP36_architectureType = 1423
   CP37_architectureGraphicRepresentationType = 1424
   CP38_architectureRepresentationObject = 1425
   CP39_architectureAlphaNumericRepresentationType = 1426
   CP40_historicCentre = 1427
   CP41_environmentalObservableEntity = 1703
   CP44_constructionSite = 1704
   CP42_materialDecay = 1705
   CP43_structuralDamage = 1706
   CP45_architectureProject = 1707
   CP46_buildingActivity = 1708
   CP49_urbanPlan = 1715
   C67_animal = 1753
   C68_biologicalObjectClassificationType = 1754
   C35_propositionalObjectType = 1768

classes = PkClass()

ontology.properties.append(OntoObject(7, "took place on or within", "P8"))
ontology.properties.append(OntoObject(83, "has formed", "P95"))
ontology.properties.append(OntoObject(87, "dissolved", "P99"))
ontology.properties.append(OntoObject(88, "was death of", "P100"))
ontology.properties.append(OntoObject(107, "meets in time with", "P119"))
ontology.properties.append(OntoObject(108, "occurs before", "P120"))
ontology.properties.append(OntoObject(115, "has broader term", "P127"))
ontology.properties.append(OntoObject(131, "joined", "P143"))
ontology.properties.append(OntoObject(132, "joined with", "P144"))
ontology.properties.append(OntoObject(133, "separated", "P145"))
ontology.properties.append(OntoObject(134, "separated from", "P146"))
ontology.properties.append(OntoObject(139, "was formed from", "P151"))
ontology.properties.append(OntoObject(991, "created", "R17"))
ontology.properties.append(OntoObject(992, "created", "R18"))
ontology.properties.append(OntoObject(1066, "has location type", "P19"))
ontology.properties.append(OntoObject(1177, "is location of", "P17"))
ontology.properties.append(OntoObject(1178, "is location at", "P15"))
ontology.properties.append(OntoObject(1188, "was a membership of", "P1"))
ontology.properties.append(OntoObject(1189, "was membership in", "P2"))
ontology.properties.append(OntoObject(1190, "has construction type", "P9"))
ontology.properties.append(OntoObject(1203, "has event type", "P47"))
ontology.properties.append(OntoObject(1204, "has group type", "P7"))
ontology.properties.append(OntoObject(1357, "is part of", "P5"))
ontology.properties.append(OntoObject(1413, "has membership type", "P3"))
ontology.properties.append(OntoObject(1640, "has currency", "P16"))
ontology.properties.append(OntoObject(1798, "has location reason", "P46"))
ontology.properties.append(OntoObject(1, "is identified by", "P1"))
ontology.properties.append(OntoObject(4, "has time-span", "P4"))
ontology.properties.append(OntoObject(63, "has language", "P72"))
ontology.properties.append(OntoObject(71, "ongoing throughout", "P81"))
ontology.properties.append(OntoObject(72, "at some time within", "P82"))
ontology.properties.append(OntoObject(78, "has value", "P90"))
ontology.properties.append(OntoObject(145, "is temporally specified by", "P164"))
ontology.properties.append(OntoObject(146, "incorporates", "P165"))
ontology.properties.append(OntoObject(147, "was a presence of", "P166"))
ontology.properties.append(OntoObject(148, "was within", "P167"))
ontology.properties.append(OntoObject(150, "end of the begin", "P81a"))
ontology.properties.append(OntoObject(151, "begin of the end", "P81b"))
ontology.properties.append(OntoObject(152, "begin of the begin", "P82a"))
ontology.properties.append(OntoObject(153, "end of the end", "P82b"))
ontology.properties.append(OntoObject(979, "carriers provided by", "R4"))
ontology.properties.append(OntoObject(982, "is example of", "R7"))
ontology.properties.append(OntoObject(1016, "is representative manifestation singleton for", "R42"))
ontology.properties.append(OntoObject(1110, "has geographical place kind", "P20"))
ontology.properties.append(OntoObject(1111, "is appellation for language of", "P11"))
ontology.properties.append(OntoObject(1112, "used in language", "P12"))
ontology.properties.append(OntoObject(1113, "refers to name", "P13"))
ontology.properties.append(OntoObject(1205, "has manifestation singleton type", "P6"))
ontology.properties.append(OntoObject(1206, "has type of manifestation product type", "P5"))
ontology.properties.append(OntoObject(1214, "has expression type", "P4"))
ontology.properties.append(OntoObject(1246, "has argument method", "P15"))
ontology.properties.append(OntoObject(1305, "is server response to request", "P4"))
ontology.properties.append(OntoObject(1316, "has carrier provided by", "P5"))
ontology.properties.append(OntoObject(1317, "is part of", "P4"))
ontology.properties.append(OntoObject(1320, "has expression portion type", "P5"))
ontology.properties.append(OntoObject(1321, "has item type", "P2"))
ontology.properties.append(OntoObject(1323, "has web request type", "P8"))
ontology.properties.append(OntoObject(1430, "has appellation for language type", "P14"))
ontology.properties.append(OntoObject(1440, "tagged by", "P12"))
ontology.properties.append(OntoObject(1499, "should be merged with", "P13"))
ontology.properties.append(OntoObject(1612, "has time unit", "P10"))
ontology.properties.append(OntoObject(1635, "has numeric dimension type", "P11"))
ontology.properties.append(OntoObject(1760, "has web address", "P16"))
ontology.properties.append(OntoObject(1761, "has short title", "P17"))
ontology.properties.append(OntoObject(1783, "has identifier type", "P19"))
ontology.properties.append(OntoObject(1837, "is role of", "P15"))
ontology.properties.append(OntoObject(1838, "is asserted by", "P16"))
ontology.properties.append(OntoObject(1839, "is qualified by", "P17"))
ontology.properties.append(OntoObject(1840, "is in the role of", "P18"))
ontology.properties.append(OntoObject(1841, "has style", "P19"))
ontology.properties.append(OntoObject(1842, "same as external identifier", "P20"))
ontology.properties.append(OntoObject(1843, "has value", "P21"))
ontology.properties.append(OntoObject(1844, "is about", "P55"))
ontology.properties.append(OntoObject(1845, "belongs to", "P56"))
ontology.properties.append(OntoObject(1846, "has preferred type", "P63"))
ontology.properties.append(OntoObject(1887, "has issue", "P20"))
ontology.properties.append(OntoObject(1943, "same as URI [owl:sameAs]", "P28"))
ontology.properties.append(OntoObject(2124, "classifies", "P68"))
ontology.properties.append(OntoObject(2125, "classifies with", "P64"))
ontology.properties.append(OntoObject(2283, "could be the same entity as", "P71"))
ontology.properties.append(OntoObject(2899, "has main language", "P32"))
ontology.properties.append(OntoObject(1335, "had departure place", "P1"))
ontology.properties.append(OntoObject(1336, "had arrival place", "P2"))
ontology.properties.append(OntoObject(1337, "has ship type", "P6"))
ontology.properties.append(OntoObject(1338, "was carried out by", "P3"))
ontology.properties.append(OntoObject(1339, "took place at", "P4"))
ontology.properties.append(OntoObject(1340, "was part of", "P5"))
ontology.properties.append(OntoObject(1341, "has built", "P7"))
ontology.properties.append(OntoObject(1342, "carried out by", "P8"))
ontology.properties.append(OntoObject(1343, "is carried out in the context of", "P9"))
ontology.properties.append(OntoObject(1345, "is participation in", "P11"))
ontology.properties.append(OntoObject(1354, "has set up", "P10"))
ontology.properties.append(OntoObject(1358, "carried", "P11"))
ontology.properties.append(OntoObject(1359, "participated in", "P12"))
ontology.properties.append(OntoObject(2, "has type", "P2"))
ontology.properties.append(OntoObject(6, "took place at", "P7"))
ontology.properties.append(OntoObject(11, "occurred in the presence of", "P12"))
ontology.properties.append(OntoObject(13, "carried out by", "P14"))
ontology.properties.append(OntoObject(14, "was influenced by", "P15"))
ontology.properties.append(OntoObject(15, "used specific object", "P16"))
ontology.properties.append(OntoObject(31, "used specific technique", "P33"))
ontology.properties.append(OntoObject(41, "has condition", "P44"))
ontology.properties.append(OntoObject(43, "is composed of", "P46"))
ontology.properties.append(OntoObject(44, "has preferred identifier", "P48"))
ontology.properties.append(OntoObject(58, "refers to", "P67"))
ontology.properties.append(OntoObject(61, "documents", "P70"))
ontology.properties.append(OntoObject(86, "brought into life", "P98"))
ontology.properties.append(OntoObject(90, "has title", "P102"))
ontology.properties.append(OntoObject(117, "is about", "P129"))
ontology.properties.append(OntoObject(119, "is identified by", "P131"))
ontology.properties.append(OntoObject(122, "continued", "P134"))
ontology.properties.append(OntoObject(1378, "has occupation", "readP1"))
ontology.properties.append(OntoObject(1379, "is nationality of", "readP2"))
ontology.properties.append(OntoObject(1380, "has gender", "readP3"))
ontology.properties.append(OntoObject(1381, "is religion of", "readP4"))
ontology.properties.append(OntoObject(1382, "is genre of", "readP5"))
ontology.properties.append(OntoObject(1383, "is provenance of", "readP6"))
ontology.properties.append(OntoObject(1384, "is status of", "readP7"))
ontology.properties.append(OntoObject(1385, "is frequency of", "readP8"))
ontology.properties.append(OntoObject(1386, "is intensity of", "readP9"))
ontology.properties.append(OntoObject(1415, "is outcome of", "readP10"))
ontology.properties.append(OntoObject(1429, "has gender", "P23"))
ontology.properties.append(OntoObject(1441, "is occupation of", "P4"))
ontology.properties.append(OntoObject(1442, "is about", "P5"))
ontology.properties.append(OntoObject(1453, "is disposition of", "readP11"))
ontology.properties.append(OntoObject(1454, "is habit of", "readP12"))
ontology.properties.append(OntoObject(1455, "is skill of", "readP13"))
ontology.properties.append(OntoObject(1493, "precedes", "readP14"))
ontology.properties.append(OntoObject(1494, "is aim of", "readP15"))
ontology.properties.append(OntoObject(1496, "is part of", "readP17"))
ontology.properties.append(OntoObject(1747, "has skill", "P38"))
ontology.properties.append(OntoObject(1768, "is age of", "readP21"))
ontology.properties.append(OntoObject(1769, "is citizenship of", "readP22"))
ontology.properties.append(OntoObject(1770, "is educational level of", "readP23"))
ontology.properties.append(OntoObject(1771, "is member of", "readP24"))
ontology.properties.append(OntoObject(1772, "is member of", "readP25"))
ontology.properties.append(OntoObject(1773, "is medium of", "readP26"))
ontology.properties.append(OntoObject(1775, "is triggered by", "readP27"))
ontology.properties.append(OntoObject(1776, "is triggered by", "readP28"))
ontology.properties.append(OntoObject(3, "has note", "P3"))
ontology.properties.append(OntoObject(5, "consists of", "P5"))
ontology.properties.append(OntoObject(8, "consists of", "P9"))
ontology.properties.append(OntoObject(9, "falls within", "P10"))
ontology.properties.append(OntoObject(10, "had participant", "P11"))
ontology.properties.append(OntoObject(12, "destroyed", "P13"))
ontology.properties.append(OntoObject(16, "was motivated by", "P17"))
ontology.properties.append(OntoObject(17, "was intended use of", "P19"))
ontology.properties.append(OntoObject(18, "had specific purpose", "P20"))
ontology.properties.append(OntoObject(19, "had general purpose", "P21"))
ontology.properties.append(OntoObject(20, "transferred title to", "P22"))
ontology.properties.append(OntoObject(21, "transferred title from", "P23"))
ontology.properties.append(OntoObject(22, "transferred title of", "P24"))
ontology.properties.append(OntoObject(23, "moved", "P25"))
ontology.properties.append(OntoObject(24, "moved to", "P26"))
ontology.properties.append(OntoObject(25, "moved from", "P27"))
ontology.properties.append(OntoObject(26, "custody surrendered by", "P28"))
ontology.properties.append(OntoObject(27, "custody received by", "P29"))
ontology.properties.append(OntoObject(28, "transferred custody of", "P30"))
ontology.properties.append(OntoObject(29, "has modified", "P31"))
ontology.properties.append(OntoObject(30, "used general technique", "P32"))
ontology.properties.append(OntoObject(32, "concerned", "P34"))
ontology.properties.append(OntoObject(33, "has identified", "P35"))
ontology.properties.append(OntoObject(34, "assigned", "P37"))
ontology.properties.append(OntoObject(35, "deassigned", "P38"))
ontology.properties.append(OntoObject(36, "measured", "P39"))
ontology.properties.append(OntoObject(37, "observed dimension", "P40"))
ontology.properties.append(OntoObject(38, "classified", "P41"))
ontology.properties.append(OntoObject(39, "assigned", "P42"))
ontology.properties.append(OntoObject(40, "has dimension", "P43"))
ontology.properties.append(OntoObject(42, "consists of", "P45"))
ontology.properties.append(OntoObject(48, "has current owner", "P52"))
ontology.properties.append(OntoObject(49, "has former or current location", "P53"))
ontology.properties.append(OntoObject(51, "has current location", "P55"))
ontology.properties.append(OntoObject(52, "bears feature", "P56"))
ontology.properties.append(OntoObject(54, "has section definition", "P58"))
ontology.properties.append(OntoObject(55, "has section", "P59"))
ontology.properties.append(OntoObject(56, "depicts", "P62"))
ontology.properties.append(OntoObject(57, "shows visual item", "P65"))
ontology.properties.append(OntoObject(59, "foresees use of", "P68"))
ontology.properties.append(OntoObject(60, "has association with", "P69"))
ontology.properties.append(OntoObject(64, "has translation", "P73"))
ontology.properties.append(OntoObject(66, "possesses", "P75"))
ontology.properties.append(OntoObject(67, "has contact point", "P76"))
ontology.properties.append(OntoObject(68, "is identified by", "P78"))
ontology.properties.append(OntoObject(69, "beginning is qualified by", "P79"))
ontology.properties.append(OntoObject(70, "end is qualified by", "P80"))
ontology.properties.append(OntoObject(73, "had at least duration", "P83"))
ontology.properties.append(OntoObject(74, "had at most duration", "P84"))
ontology.properties.append(OntoObject(75, "falls within", "P86"))
ontology.properties.append(OntoObject(76, "is identified by", "P87"))
ontology.properties.append(OntoObject(77, "falls within", "P89"))
ontology.properties.append(OntoObject(79, "has unit", "P91"))
ontology.properties.append(OntoObject(81, "took out of existence", "P93"))
ontology.properties.append(OntoObject(82, "has created", "P94"))
ontology.properties.append(OntoObject(84, "by mother", "P96"))
ontology.properties.append(OntoObject(85, "from father", "P97"))
ontology.properties.append(OntoObject(89, "had as general use", "P101"))
ontology.properties.append(OntoObject(91, "was intended for", "P103"))
ontology.properties.append(OntoObject(92, "is subject to", "P104"))
ontology.properties.append(OntoObject(93, "right held by", "P105"))
ontology.properties.append(OntoObject(94, "is composed of", "P106"))
ontology.properties.append(OntoObject(95, "has current or former member", "P107"))
ontology.properties.append(OntoObject(96, "has produced", "P108"))
ontology.properties.append(OntoObject(98, "augmented", "P110"))
ontology.properties.append(OntoObject(99, "added", "P111"))
ontology.properties.append(OntoObject(100, "diminished", "P112"))
ontology.properties.append(OntoObject(101, "removed", "P113"))
ontology.properties.append(OntoObject(102, "is equal in time to", "P114"))
ontology.properties.append(OntoObject(103, "finishes", "P115"))
ontology.properties.append(OntoObject(104, "starts", "P116"))
ontology.properties.append(OntoObject(105, "occurs during", "P117"))
ontology.properties.append(OntoObject(106, "overlaps in time with", "P118"))
ontology.properties.append(OntoObject(109, "overlaps with", "P121"))
ontology.properties.append(OntoObject(110, "borders with", "P122"))
ontology.properties.append(OntoObject(111, "resulted in", "P123"))
ontology.properties.append(OntoObject(112, "transformed", "P124"))
ontology.properties.append(OntoObject(113, "used object of type", "P125"))
ontology.properties.append(OntoObject(114, "employed", "P126"))
ontology.properties.append(OntoObject(116, "carries", "P128"))
ontology.properties.append(OntoObject(118, "shows features of", "P130"))
ontology.properties.append(OntoObject(123, "created type", "P135"))
ontology.properties.append(OntoObject(124, "was based on", "P136"))
ontology.properties.append(OntoObject(125, "exemplifies", "P137"))
ontology.properties.append(OntoObject(126, "represents", "P138"))
ontology.properties.append(OntoObject(127, "has alternative form", "P139"))
ontology.properties.append(OntoObject(128, "assigned attribute to", "P140"))
ontology.properties.append(OntoObject(129, "assigned", "P141"))
ontology.properties.append(OntoObject(130, "used constituent", "P142"))
ontology.properties.append(OntoObject(135, "curated", "P147"))
ontology.properties.append(OntoObject(136, "has component", "P148"))
ontology.properties.append(OntoObject(137, "is identified by", "P149"))
ontology.properties.append(OntoObject(1042, "has quantifiable quality", "P22"))
ontology.properties.append(OntoObject(1247, "used as premise", "J1"))
ontology.properties.append(OntoObject(1248, "conclued that", "J2"))
ontology.properties.append(OntoObject(1249, "applies", "J3"))
ontology.properties.append(OntoObject(1250, "that", "J4"))
ontology.properties.append(OntoObject(1251, "holds to be", "J5"))
ontology.properties.append(OntoObject(1394, "assigned object type", "L1"))
ontology.properties.append(OntoObject(1396, "has yarn type", "L3"))
ontology.properties.append(OntoObject(1397, "assigned domain type", "L4"))
ontology.properties.append(OntoObject(1398, "has twist type", "L5"))
ontology.properties.append(OntoObject(1399, "has warp type", "L6"))
ontology.properties.append(OntoObject(1400, "used warp", "L7"))
ontology.properties.append(OntoObject(1401, "used weave", "L8"))
ontology.properties.append(OntoObject(1402, "used weft", "L9"))
ontology.properties.append(OntoObject(1403, "used yarn", "L10"))
ontology.properties.append(OntoObject(1404, "has weave type", "L11"))
ontology.properties.append(OntoObject(1405, "has motif type", "L12"))
ontology.properties.append(OntoObject(1406, "has warping type (deprecated)", "L13"))
ontology.properties.append(OntoObject(1407, "used specific weaving technique", "L14"))
ontology.properties.append(OntoObject(1408, "has weft type", "L15"))
ontology.properties.append(OntoObject(1410, "has quality type", "P23"))
ontology.properties.append(OntoObject(1411, "pertains to", "P13"))
ontology.properties.append(OntoObject(1414, "is life of", "P26"))
ontology.properties.append(OntoObject(1435, "stemmed from", "P22"))
ontology.properties.append(OntoObject(1436, "had partner", "P20"))
ontology.properties.append(OntoObject(1437, "has type of interaction", "P21"))
ontology.properties.append(OntoObject(1439, "has its origins in", "P24"))
ontology.properties.append(OntoObject(1599, "took place at", "P6"))
ontology.properties.append(OntoObject(1851, "has specific location", "P48"))
ontology.properties.append(OntoObject(1852, "has location", "P49"))
ontology.properties.append(OntoObject(1854, "has legal location type", "P51"))
ontology.properties.append(OntoObject(1881, "is location in or on", "P52"))
ontology.properties.append(OntoObject(1085, "encountered object", "O19"))
ontology.properties.append(OntoObject(1658, "has use type", "P29"))
ontology.properties.append(OntoObject(1661, "is use of", "P32"))
ontology.properties.append(OntoObject(1860, "is physical man-made thing type of", "P1"))
ontology.properties.append(OntoObject(1431, "the investigation concerns", "P1"))
ontology.properties.append(OntoObject(1432, "is requested as a witness", "P2"))
ontology.properties.append(OntoObject(1433, "is documented in", "P3"))
ontology.properties.append(OntoObject(1516, "has motivation", "P4"))
ontology.properties.append(OntoObject(1517, "has motivation type", "P5"))
ontology.properties.append(OntoObject(1613, "has duration", "P6"))
ontology.properties.append(OntoObject(1616, "mentions geographical place", "P7"))
ontology.properties.append(OntoObject(1617, "concerns", "P8"))
ontology.properties.append(OntoObject(1618, "has time lapse before account", "P9"))
ontology.properties.append(OntoObject(1619, "refers to", "P10"))
ontology.properties.append(OntoObject(1620, "has frequency classification", "P11"))
ontology.properties.append(OntoObject(1621, "has as a minimum duration", "P12"))
ontology.properties.append(OntoObject(1622, "has as a maximum duration", "P13"))
ontology.properties.append(OntoObject(1623, "has time lapse of last journey before account", "P14"))
ontology.properties.append(OntoObject(1627, "has marital status", "P15"))
ontology.properties.append(OntoObject(1892, "has intermediary", "P16"))
ontology.properties.append(OntoObject(1040, "effects", "P3"))
ontology.properties.append(OntoObject(1041, "ends", "P4"))
ontology.properties.append(OntoObject(1344, "is participation of", "P10"))
ontology.properties.append(OntoObject(1346, "is participation in the quality of", "P12"))
ontology.properties.append(OntoObject(1409, "involves partner", "P15"))
ontology.properties.append(OntoObject(1434, "has relationship type", "P16"))
ontology.properties.append(OntoObject(1445, "has relationship source", "P17"))
ontology.properties.append(OntoObject(1446, "has relationship target", "P18"))
ontology.properties.append(OntoObject(1784, "is interaction of", "P41"))
ontology.properties.append(OntoObject(2270, "has quality during membership", "P63"))
ontology.properties.append(OntoObject(2896, "has role quality", "P72"))
ontology.properties.append(OntoObject(2897, "is social relationship role of", "P73"))
ontology.properties.append(OntoObject(2898, "is role within", "P74"))
ontology.properties.append(OntoObject(120, "spatiotemporally overlaps with", "P132"))
ontology.properties.append(OntoObject(1412, "has social quality", "P14"))
ontology.properties.append(OntoObject(1443, "takes place at", "P6"))
ontology.properties.append(OntoObject(1444, "on behalf of", "P7"))
ontology.properties.append(OntoObject(1863, "belongs to activity domain", "P55"))
ontology.properties.append(OntoObject(1598, "has type", "P1"))
ontology.properties.append(OntoObject(1636, "has measurement unit", "P12"))
ontology.properties.append(OntoObject(1637, "has measurement unit", "P13"))
ontology.properties.append(OntoObject(1638, "has measurement unit", "P14"))
ontology.properties.append(OntoObject(1639, "has measurement unit", "P15"))
ontology.properties.append(OntoObject(1653, "effects", "P8"))
ontology.properties.append(OntoObject(1654, "ends", "P9"))
ontology.properties.append(OntoObject(1655, "belongs to", "P27"))
ontology.properties.append(OntoObject(1656, "has part", "P28"))
ontology.properties.append(OntoObject(1657, "is composed of part of type", "P17"))
ontology.properties.append(OntoObject(1659, "is use by", "P30"))
ontology.properties.append(OntoObject(1660, "has purpose", "P31"))
ontology.properties.append(OntoObject(993, "created a realisation of", "R19"))
ontology.properties.append(OntoObject(1015, "has representative manifestation product type", "R41"))
ontology.properties.append(OntoObject(1595, "used specific expression", "P1"))
ontology.properties.append(OntoObject(1596, "created manifestation", "P2"))
ontology.properties.append(OntoObject(1597, "published the work of", "P3"))
ontology.properties.append(OntoObject(1644, "requires the use of", "P6"))
ontology.properties.append(OntoObject(1645, "has material", "P7"))
ontology.properties.append(OntoObject(1646, "has volume", "P8"))
ontology.properties.append(OntoObject(1647, "has planned duration", "P9"))
ontology.properties.append(OntoObject(1648, "has weight", "P10"))
ontology.properties.append(OntoObject(1649, "shall be performed after", "P11"))
ontology.properties.append(OntoObject(1650, "has step type", "P12"))
ontology.properties.append(OntoObject(1651, "has procedure type", "P13"))
ontology.properties.append(OntoObject(1652, "foresees the use of specific object", "P14"))
ontology.properties.append(OntoObject(1748, "is connotation of", "P39"))
ontology.properties.append(OntoObject(2921, "classifies with", "P34"))
ontology.properties.append(OntoObject(2923, "is realised in", "P35"))
ontology.properties.append(OntoObject(1609, "is defined in relation to", "P19"))
ontology.properties.append(OntoObject(1610, "is subjection of", "P8"))
ontology.properties.append(OntoObject(1611, "is right of", "P9"))
ontology.properties.append(OntoObject(1626, "is embodiment by", "P26"))
ontology.properties.append(OntoObject(1630, "has holding of a right type", "P29"))
ontology.properties.append(OntoObject(1632, "realizes", "P31"))
ontology.properties.append(OntoObject(1634, "is embodiment of", "P33"))
ontology.properties.append(OntoObject(1643, "is defined by", "P35"))
ontology.properties.append(OntoObject(1739, "pertains to", "P36"))
ontology.properties.append(OntoObject(1777, "involves legal quality", "P37"))
ontology.properties.append(OntoObject(1778, "has legal connotation type", "P38"))
ontology.properties.append(OntoObject(1779, "has type", "P39"))
ontology.properties.append(OntoObject(1785, "has maximal projection in geographical space", "P45"))
ontology.properties.append(OntoObject(1807, "is acquisition by", "P43"))
ontology.properties.append(OntoObject(1808, "is acquisition of", "P44"))
ontology.properties.append(OntoObject(1809, "issued by", "P45"))
ontology.properties.append(OntoObject(1810, "has legal quality acquisition type", "P46"))
ontology.properties.append(OntoObject(1853, "has social role type", "P50"))
ontology.properties.append(OntoObject(1857, "is legal connotation of", "P52"))
ontology.properties.append(OntoObject(1944, "is in relation to", "P62"))
ontology.properties.append(OntoObject(2416, "is defined in the context of", "P69"))
ontology.properties.append(OntoObject(2436, "is embodied in", "P70"))
ontology.properties.append(OntoObject(2437, "has political or administrative entity type", "P71"))
ontology.properties.append(OntoObject(1631, "is validity of", "P30"))
ontology.properties.append(OntoObject(1633, "has custom or law type", "P32"))
ontology.properties.append(OntoObject(1780, "is valid in", "P40"))
ontology.properties.append(OntoObject(1500, "belongs to", "P14"))
ontology.properties.append(OntoObject(1781, "is valid identifier of", "P18"))
ontology.properties.append(OntoObject(1782, "is identification of", "P18"))
ontology.properties.append(OntoObject(1095, "removed part or all of", "AP5"))
ontology.properties.append(OntoObject(1107, "is embedding of", "AP18"))
ontology.properties.append(OntoObject(1108, "is embedding in", "AP19"))
ontology.properties.append(OntoObject(1799, "has archeological excavation type", "P1"))
ontology.properties.append(OntoObject(1801, "has excavation process unit type", "P2"))
ontology.properties.append(OntoObject(1802, "overlies", "P3"))
ontology.properties.append(OntoObject(1803, "cuts", "P4"))
ontology.properties.append(OntoObject(1600, "is section of", "BP1"))
ontology.properties.append(OntoObject(1742, "has quality dimension", "P35"))
ontology.properties.append(OntoObject(1894, "has dimension kind", "P25"))
ontology.properties.append(OntoObject(1826, "concerns", "P6"))
ontology.properties.append(OntoObject(1827, "is carried out by", "P7"))
ontology.properties.append(OntoObject(1828, "carried out at", "P8"))
ontology.properties.append(OntoObject(1829, "has rank", "P9"))
ontology.properties.append(OntoObject(1830, "has as disciplinary area", "P10"))
ontology.properties.append(OntoObject(1805, "is study at", "P1"))
ontology.properties.append(OntoObject(1806, "is the study by", "P2"))
ontology.properties.append(OntoObject(1811, "was obtained by", "P3"))
ontology.properties.append(OntoObject(1812, "is obtention of", "P4"))
ontology.properties.append(OntoObject(1815, "has academic supervisor", "P5"))
ontology.properties.append(OntoObject(1831, "is delivered by", "P11"))
ontology.properties.append(OntoObject(1832, "is study of", "P12"))
ontology.properties.append(OntoObject(1833, "is obtained at", "P13"))
ontology.properties.append(OntoObject(2932, "classifies with", "P87"))
ontology.properties.append(OntoObject(2933, "classifies", "P88"))
ontology.properties.append(OntoObject(1847, "take care of", "P1"))
ontology.properties.append(OntoObject(1848, "has caretaker", "P2"))
ontology.properties.append(OntoObject(1849, "concerned person", "P3"))
ontology.properties.append(OntoObject(1850, "concerned school", "P4"))
ontology.properties.append(OntoObject(1855, "has taking care type", "P5"))
ontology.properties.append(OntoObject(1856, "has attending a school type", "P6"))
ontology.properties.append(OntoObject(1642, "is participation on behalf of", "P34"))
ontology.properties.append(OntoObject(1893, "is quality in relation to", "P57"))
ontology.properties.append(OntoObject(1216, "is reproduction of", "P1"))
ontology.properties.append(OntoObject(1334, "refers to", "P9"))
ontology.properties.append(OntoObject(1762, "has definition", "P18"))
ontology.properties.append(OntoObject(1763, "has comment", "P19"))
ontology.properties.append(OntoObject(1864, "has value version", "P20"))
ontology.properties.append(OntoObject(1865, "has text type", "P21"))
ontology.properties.append(OntoObject(1866, "has comment type", "P22"))
ontology.properties.append(OntoObject(1872, "is annotated in", "P23"))
ontology.properties.append(OntoObject(1874, "at position", "P24"))
ontology.properties.append(OntoObject(1875, "annotated entity", "P25"))
ontology.properties.append(OntoObject(1876, "mentions", "P26"))
ontology.properties.append(OntoObject(1877, "is mentioned in", "P27"))
ontology.properties.append(OntoObject(1878, "at position", "P28"))
ontology.properties.append(OntoObject(1879, "has value", "P29"))
ontology.properties.append(OntoObject(1889, "is about", "P30"))
ontology.properties.append(OntoObject(2214, "has datation value", "P26"))
ontology.properties.append(OntoObject(2272, "has datation type", "P27"))
ontology.properties.append(OntoObject(2415, "has mentioning content", "P31"))
ontology.properties.append(OntoObject(140, "has parent", "P152"))
ontology.properties.append(OntoObject(1871, "comprend", "P8"))
ontology.properties.append(OntoObject(1895, "has information object type", "P26"))
ontology.properties.append(OntoObject(1922, "effects dedication", "P21"))
ontology.properties.append(OntoObject(1923, "has dedicatory object", "P22"))
ontology.properties.append(OntoObject(1924, "has dedicatee", "P23"))
ontology.properties.append(OntoObject(1925, "has conceptual dedicatee", "P24"))
ontology.properties.append(OntoObject(1926, "has beneficiary", "P25"))
ontology.properties.append(OntoObject(1039, "included performed version of", "R66"))
ontology.properties.append(OntoObject(1927, "is about", "P58"))
ontology.properties.append(OntoObject(1928, "is quality of", "P59"))
ontology.properties.append(OntoObject(1930, "is quality on behalf of", "P61"))
ontology.properties.append(OntoObject(1931, "has performance type", "P27"))
ontology.properties.append(OntoObject(1797, "has activity type", "P19"))
ontology.properties.append(OntoObject(2109, "moved from", "P60"))
ontology.properties.append(OntoObject(2110, "moved to", "P61"))
ontology.properties.append(OntoObject(2111, "displaces", "P62"))
ontology.properties.append(OntoObject(2112, "has move identifying type", "P29"))
ontology.properties.append(OntoObject(2116, "is movement of", "P1"))
ontology.properties.append(OntoObject(2117, "has movement identifying type", "P2"))
ontology.properties.append(OntoObject(2118, "has stopover identifying type", "P3"))
ontology.properties.append(OntoObject(2119, "is journey of", "P4"))
ontology.properties.append(OntoObject(2120, "has carrier's journey identifying type", "P5"))
ontology.properties.append(OntoObject(2121, "is coerced displacement of", "P6"))
ontology.properties.append(OntoObject(2122, "has actor's coerced trip identifying type", "P7"))
ontology.properties.append(OntoObject(2123, "is continuation of", "P8"))
ontology.properties.append(OntoObject(1075, "observed property type", "O9"))
ontology.properties.append(OntoObject(2128, "observed entity type", "P30"))
ontology.properties.append(OntoObject(1183, "at distance", "P16"))
ontology.properties.append(OntoObject(1945, "is inside or relative to", "P57"))
ontology.properties.append(OntoObject(1946, "has relative location type", "P58"))
ontology.properties.append(OntoObject(1947, "is quality of", "P59"))
ontology.properties.append(OntoObject(2257, "was or is composed of object of type", "P66"))
ontology.properties.append(OntoObject(1641, "is intention of", "P7"))
ontology.properties.append(OntoObject(2299, "classifies", "P72"))
ontology.properties.append(OntoObject(2300, "classifies with", "P73"))
ontology.properties.append(OntoObject(2274, "has type of participation", "P64"))
ontology.properties.append(OntoObject(2312, "planned move from", "P28"))
ontology.properties.append(OntoObject(2313, "planned move to", "P29"))
ontology.properties.append(OntoObject(2314, "has component dimension", "P30"))
ontology.properties.append(OntoObject(2315, "has quantifiable component type", "P31"))
ontology.properties.append(OntoObject(2310, "has epistemic situation preferred type", "P74"))
ontology.properties.append(OntoObject(2316, "is quantifiable quality of", "P76"))
ontology.properties.append(OntoObject(2317, "is involvement in", "P77"))
ontology.properties.append(OntoObject(2318, "has involvement type", "P78"))
ontology.properties.append(OntoObject(2319, "is involvement of", "P79"))
ontology.properties.append(OntoObject(2311, "is quantifiable quality of", "P75"))
ontology.properties.append(OntoObject(2320, "is linked to", "P80"))
ontology.properties.append(OntoObject(2321, "has link type", "P81"))
ontology.properties.append(OntoObject(2324, "classifies", "P82"))
ontology.properties.append(OntoObject(2325, "classifies with", "P83"))
ontology.properties.append(OntoObject(2368, "has participation relation type", "P65"))
ontology.properties.append(OntoObject(2369, "is participation relation of", "P66"))
ontology.properties.append(OntoObject(2370, "is role in", "P67"))
ontology.properties.append(OntoObject(2371, "has role quality", "P68"))
ontology.properties.append(OntoObject(1741, "has content", "P34"))
ontology.properties.append(OntoObject(1800, "has intentional expression identifying type", "P48"))
ontology.properties.append(OntoObject(2941, "is quantifiable quality of", "P89"))
ontology.properties.append(OntoObject(45, "has former or current keeper", "P49"))
ontology.properties.append(OntoObject(46, "has current keeper", "P50"))
ontology.properties.append(OntoObject(47, "has former or current owner", "P51"))
ontology.properties.append(OntoObject(62, "lists", "P71"))
ontology.properties.append(OntoObject(80, "brought into existence", "P92"))
ontology.properties.append(OntoObject(141, "occupies", "P156"))
ontology.properties.append(OntoObject(142, "is at rest relative to", "P157"))
ontology.properties.append(OntoObject(1067, "diminished", "O1"))
ontology.properties.append(OntoObject(1078, "has dimension", "O12"))
ontology.properties.append(OntoObject(1081, "occupied", "O15"))
ontology.properties.append(OntoObject(1918, "was a presence of", "P195"))
ontology.properties.append(OntoObject(1919, "defines", "P196"))
ontology.properties.append(OntoObject(1921, "holds or supports", "P198"))
ontology.properties.append(OntoObject(2113, "contains", "O25"))
ontology.properties.append(OntoObject(2327, "affects", "pc1"))
ontology.properties.append(OntoObject(2328, "has connection through", "pc3"))
ontology.properties.append(OntoObject(2329, "shows building feature", "pc4"))
ontology.properties.append(OntoObject(2332, "is connected through", "pc7"))
ontology.properties.append(OntoObject(2333, "is connected to", "pc8"))
ontology.properties.append(OntoObject(2335, "belongs to", "pc10"))
ontology.properties.append(OntoObject(2338, "is regulated by", "pc13"))
ontology.properties.append(OntoObject(2340, "shows plan configuration type", "pc15"))
ontology.properties.append(OntoObject(2341, "shows structural system", "pc16"))
ontology.properties.append(OntoObject(2342, "has performance efficiency documented in", "pc17"))
ontology.properties.append(OntoObject(2343, "has physical relation with", "pc18"))
ontology.properties.append(OntoObject(2347, "shows building homogeneity with", "pc20"))
ontology.properties.append(OntoObject(2348, "addressed", "pc21"))
ontology.properties.append(OntoObject(2349, "has type", "pc21_1"))
ontology.properties.append(OntoObject(2352, "occurred in", "pc24"))
ontology.properties.append(OntoObject(2353, "occurs in", "pc25"))
ontology.properties.append(OntoObject(2354, "is illustrated by", "pc26"))
ontology.properties.append(OntoObject(2358, "resulted in", "pc30"))
ontology.properties.append(OntoObject(2359, "transformed", "pc31"))
ontology.properties.append(OntoObject(2380, "was embodied by", "pc42"))
ontology.properties.append(OntoObject(2873, "shows as construction component", "pc67"))
ontology.properties.append(OntoObject(2922, "is of biological object classification type", "P86"))
ontology.properties.append(OntoObject(2934, "has propositional object type", "P32"))

class PkProperty:
   P8_tookPlaceOnOrWithin = 7
   P95_hasFormed = 83
   P99_dissolved = 87
   P100_wasDeathOf = 88
   P119_meetsInTimeWith = 107
   P120_occursBefore = 108
   P127_hasBroaderTerm = 115
   P143_joined = 131
   P144_joinedWith = 132
   P145_separated = 133
   P146_separatedFrom = 134
   P151_wasFormedFrom = 139
   R17_created = 991
   R18_created = 992
   P19_hasLocationType = 1066
   P17_isLocationOf = 1177
   P15_isLocationAt = 1178
   P1_wasAMembershipOf = 1188
   P2_wasMembershipIn = 1189
   P9_hasConstructionType = 1190
   P47_hasEventType = 1203
   P7_hasGroupType = 1204
   P5_isPartOf = 1357
   P3_hasMembershipType = 1413
   P16_hasCurrency = 1640
   P46_hasLocationReason = 1798
   P1_isIdentifiedBy = 1
   P4_hasTimeSpan = 4
   P72_hasLanguage = 63
   P81_ongoingThroughout = 71
   P82_atSomeTimeWithin = 72
   P90_hasValue = 78
   P164_isTemporallySpecifiedBy = 145
   P165_incorporates = 146
   P166_wasAPresenceOf = 147
   P167_wasWithin = 148
   P81a_endOfTheBegin = 150
   P81b_beginOfTheEnd = 151
   P82a_beginOfTheBegin = 152
   P82b_endOfTheEnd = 153
   R4_carriersProvidedBy = 979
   R7_isExampleOf = 982
   R42_isRepresentativeManifestationSingletonFor = 1016
   P20_hasGeographicalPlaceKind = 1110
   P11_isAppellationForLanguageOf = 1111
   P12_usedInLanguage = 1112
   P13_refersToName = 1113
   P6_hasManifestationSingletonType = 1205
   P5_hasTypeOfManifestationProductType = 1206
   P4_hasExpressionType = 1214
   P15_hasArgumentMethod = 1246
   P4_isServerResponseToRequest = 1305
   P5_hasCarrierProvidedBy = 1316
   P4_isPartOf = 1317
   P5_hasExpressionPortionType = 1320
   P2_hasItemType = 1321
   P8_hasWebRequestType = 1323
   P14_hasAppellationForLanguageType = 1430
   P12_taggedBy = 1440
   P13_shouldBeMergedWith = 1499
   P10_hasTimeUnit = 1612
   P11_hasNumericDimensionType = 1635
   P16_hasWebAddress = 1760
   P17_hasShortTitle = 1761
   P19_hasIdentifierType = 1783
   P15_isRoleOf = 1837
   P16_isAssertedBy = 1838
   P17_isQualifiedBy = 1839
   P18_isInTheRoleOf = 1840
   P19_hasStyle = 1841
   P20_sameAsExternalIdentifier = 1842
   P21_hasValue = 1843
   P55_isAbout = 1844
   P56_belongsTo = 1845
   P63_hasPreferredType = 1846
   P20_hasIssue = 1887
   P28_sameAsUriOwlSameas = 1943
   P68_classifies = 2124
   P64_classifiesWith = 2125
   P71_couldBeTheSameEntityAs = 2283
   P32_hasMainLanguage = 2899
   P1_hadDeparturePlace = 1335
   P2_hadArrivalPlace = 1336
   P6_hasShipType = 1337
   P3_wasCarriedOutBy = 1338
   P4_tookPlaceAt = 1339
   P5_wasPartOf = 1340
   P7_hasBuilt = 1341
   P8_carriedOutBy = 1342
   P9_isCarriedOutInTheContextOf = 1343
   P11_isParticipationIn = 1345
   P10_hasSetUp = 1354
   P11_carried = 1358
   P12_participatedIn = 1359
   P2_hasType = 2
   P7_tookPlaceAt = 6
   P12_occurredInThePresenceOf = 11
   P14_carriedOutBy = 13
   P15_wasInfluencedBy = 14
   P16_usedSpecificObject = 15
   P33_usedSpecificTechnique = 31
   P44_hasCondition = 41
   P46_isComposedOf = 43
   P48_hasPreferredIdentifier = 44
   P67_refersTo = 58
   P70_documents = 61
   P98_broughtIntoLife = 86
   P102_hasTitle = 90
   P129_isAbout = 117
   P131_isIdentifiedBy = 119
   P134_continued = 122
   readP1_hasOccupation = 1378
   readP2_isNationalityOf = 1379
   readP3_hasGender = 1380
   readP4_isReligionOf = 1381
   readP5_isGenreOf = 1382
   readP6_isProvenanceOf = 1383
   readP7_isStatusOf = 1384
   readP8_isFrequencyOf = 1385
   readP9_isIntensityOf = 1386
   readP10_isOutcomeOf = 1415
   P23_hasGender = 1429
   P4_isOccupationOf = 1441
   P5_isAbout = 1442
   readP11_isDispositionOf = 1453
   readP12_isHabitOf = 1454
   readP13_isSkillOf = 1455
   readP14_precedes = 1493
   readP15_isAimOf = 1494
   readP17_isPartOf = 1496
   P38_hasSkill = 1747
   readP21_isAgeOf = 1768
   readP22_isCitizenshipOf = 1769
   readP23_isEducationalLevelOf = 1770
   readP24_isMemberOf = 1771
   readP25_isMemberOf = 1772
   readP26_isMediumOf = 1773
   readP27_isTriggeredBy = 1775
   readP28_isTriggeredBy = 1776
   P3_hasNote = 3
   P5_consistsOf = 5
   P9_consistsOf = 8
   P10_fallsWithin = 9
   P11_hadParticipant = 10
   P13_destroyed = 12
   P17_wasMotivatedBy = 16
   P19_wasIntendedUseOf = 17
   P20_hadSpecificPurpose = 18
   P21_hadGeneralPurpose = 19
   P22_transferredTitleTo = 20
   P23_transferredTitleFrom = 21
   P24_transferredTitleOf = 22
   P25_moved = 23
   P26_movedTo = 24
   P27_movedFrom = 25
   P28_custodySurrenderedBy = 26
   P29_custodyReceivedBy = 27
   P30_transferredCustodyOf = 28
   P31_hasModified = 29
   P32_usedGeneralTechnique = 30
   P34_concerned = 32
   P35_hasIdentified = 33
   P37_assigned = 34
   P38_deassigned = 35
   P39_measured = 36
   P40_observedDimension = 37
   P41_classified = 38
   P42_assigned = 39
   P43_hasDimension = 40
   P45_consistsOf = 42
   P52_hasCurrentOwner = 48
   P53_hasFormerOrCurrentLocation = 49
   P55_hasCurrentLocation = 51
   P56_bearsFeature = 52
   P58_hasSectionDefinition = 54
   P59_hasSection = 55
   P62_depicts = 56
   P65_showsVisualItem = 57
   P68_foreseesUseOf = 59
   P69_hasAssociationWith = 60
   P73_hasTranslation = 64
   P75_possesses = 66
   P76_hasContactPoint = 67
   P78_isIdentifiedBy = 68
   P79_beginningIsQualifiedBy = 69
   P80_endIsQualifiedBy = 70
   P83_hadAtLeastDuration = 73
   P84_hadAtMostDuration = 74
   P86_fallsWithin = 75
   P87_isIdentifiedBy = 76
   P89_fallsWithin = 77
   P91_hasUnit = 79
   P93_tookOutOfExistence = 81
   P94_hasCreated = 82
   P96_byMother = 84
   P97_fromFather = 85
   P101_hadAsGeneralUse = 89
   P103_wasIntendedFor = 91
   P104_isSubjectTo = 92
   P105_rightHeldBy = 93
   P106_isComposedOf = 94
   P107_hasCurrentOrFormerMember = 95
   P108_hasProduced = 96
   P110_augmented = 98
   P111_added = 99
   P112_diminished = 100
   P113_removed = 101
   P114_isEqualInTimeTo = 102
   P115_finishes = 103
   P116_starts = 104
   P117_occursDuring = 105
   P118_overlapsInTimeWith = 106
   P121_overlapsWith = 109
   P122_bordersWith = 110
   P123_resultedIn = 111
   P124_transformed = 112
   P125_usedObjectOfType = 113
   P126_employed = 114
   P128_carries = 116
   P130_showsFeaturesOf = 118
   P135_createdType = 123
   P136_wasBasedOn = 124
   P137_exemplifies = 125
   P138_represents = 126
   P139_hasAlternativeForm = 127
   P140_assignedAttributeTo = 128
   P141_assigned = 129
   P142_usedConstituent = 130
   P147_curated = 135
   P148_hasComponent = 136
   P149_isIdentifiedBy = 137
   P22_hasQuantifiableQuality = 1042
   J1_usedAsPremise = 1247
   J2_concluedThat = 1248
   J3_applies = 1249
   J4_that = 1250
   J5_holdsToBe = 1251
   L1_assignedObjectType = 1394
   L3_hasYarnType = 1396
   L4_assignedDomainType = 1397
   L5_hasTwistType = 1398
   L6_hasWarpType = 1399
   L7_usedWarp = 1400
   L8_usedWeave = 1401
   L9_usedWeft = 1402
   L10_usedYarn = 1403
   L11_hasWeaveType = 1404
   L12_hasMotifType = 1405
   L13_hasWarpingTypeDeprecated = 1406
   L14_usedSpecificWeavingTechnique = 1407
   L15_hasWeftType = 1408
   P23_hasQualityType = 1410
   P13_pertainsTo = 1411
   P26_isLifeOf = 1414
   P22_stemmedFrom = 1435
   P20_hadPartner = 1436
   P21_hasTypeOfInteraction = 1437
   P24_hasItsOriginsIn = 1439
   P6_tookPlaceAt = 1599
   P48_hasSpecificLocation = 1851
   P49_hasLocation = 1852
   P51_hasLegalLocationType = 1854
   P52_isLocationInOrOn = 1881
   O19_encounteredObject = 1085
   P29_hasUseType = 1658
   P32_isUseOf = 1661
   P1_isPhysicalManMadeThingTypeOf = 1860
   P1_theInvestigationConcerns = 1431
   P2_isRequestedAsAWitness = 1432
   P3_isDocumentedIn = 1433
   P4_hasMotivation = 1516
   P5_hasMotivationType = 1517
   P6_hasDuration = 1613
   P7_mentionsGeographicalPlace = 1616
   P8_concerns = 1617
   P9_hasTimeLapseBeforeAccount = 1618
   P10_refersTo = 1619
   P11_hasFrequencyClassification = 1620
   P12_hasAsAMinimumDuration = 1621
   P13_hasAsAMaximumDuration = 1622
   P14_hasTimeLapseOfLastJourneyBeforeAccount = 1623
   P15_hasMaritalStatus = 1627
   P16_hasIntermediary = 1892
   P3_effects = 1040
   P4_ends = 1041
   P10_isParticipationOf = 1344
   P12_isParticipationInTheQualityOf = 1346
   P15_involvesPartner = 1409
   P16_hasRelationshipType = 1434
   P17_hasRelationshipSource = 1445
   P18_hasRelationshipTarget = 1446
   P41_isInteractionOf = 1784
   P63_hasQualityDuringMembership = 2270
   P72_hasRoleQuality = 2896
   P73_isSocialRelationshipRoleOf = 2897
   P74_isRoleWithin = 2898
   P132_spatiotemporallyOverlapsWith = 120
   P14_hasSocialQuality = 1412
   P6_takesPlaceAt = 1443
   P7_onBehalfOf = 1444
   P55_belongsToActivityDomain = 1863
   P1_hasType = 1598
   P12_hasMeasurementUnit = 1636
   P13_hasMeasurementUnit = 1637
   P14_hasMeasurementUnit = 1638
   P15_hasMeasurementUnit = 1639
   P8_effects = 1653
   P9_ends = 1654
   P27_belongsTo = 1655
   P28_hasPart = 1656
   P17_isComposedOfPartOfType = 1657
   P30_isUseBy = 1659
   P31_hasPurpose = 1660
   R19_createdARealisationOf = 993
   R41_hasRepresentativeManifestationProductType = 1015
   P1_usedSpecificExpression = 1595
   P2_createdManifestation = 1596
   P3_publishedTheWorkOf = 1597
   P6_requiresTheUseOf = 1644
   P7_hasMaterial = 1645
   P8_hasVolume = 1646
   P9_hasPlannedDuration = 1647
   P10_hasWeight = 1648
   P11_shallBePerformedAfter = 1649
   P12_hasStepType = 1650
   P13_hasProcedureType = 1651
   P14_foreseesTheUseOfSpecificObject = 1652
   P39_isConnotationOf = 1748
   P34_classifiesWith = 2921
   P35_isRealisedIn = 2923
   P19_isDefinedInRelationTo = 1609
   P8_isSubjectionOf = 1610
   P9_isRightOf = 1611
   P26_isEmbodimentBy = 1626
   P29_hasHoldingOfARightType = 1630
   P31_realizes = 1632
   P33_isEmbodimentOf = 1634
   P35_isDefinedBy = 1643
   P36_pertainsTo = 1739
   P37_involvesLegalQuality = 1777
   P38_hasLegalConnotationType = 1778
   P39_hasType = 1779
   P45_hasMaximalProjectionInGeographicalSpace = 1785
   P43_isAcquisitionBy = 1807
   P44_isAcquisitionOf = 1808
   P45_issuedBy = 1809
   P46_hasLegalQualityAcquisitionType = 1810
   P50_hasSocialRoleType = 1853
   P52_isLegalConnotationOf = 1857
   P62_isInRelationTo = 1944
   P69_isDefinedInTheContextOf = 2416
   P70_isEmbodiedIn = 2436
   P71_hasPoliticalOrAdministrativeEntityType = 2437
   P30_isValidityOf = 1631
   P32_hasCustomOrLawType = 1633
   P40_isValidIn = 1780
   P14_belongsTo = 1500
   P18_isValidIdentifierOf = 1781
   P18_isIdentificationOf = 1782
   AP5_removedPartOrAllOf = 1095
   AP18_isEmbeddingOf = 1107
   AP19_isEmbeddingIn = 1108
   P1_hasArcheologicalExcavationType = 1799
   P2_hasExcavationProcessUnitType = 1801
   P3_overlies = 1802
   P4_cuts = 1803
   BP1_isSectionOf = 1600
   P35_hasQualityDimension = 1742
   P25_hasDimensionKind = 1894
   P6_concerns = 1826
   P7_isCarriedOutBy = 1827
   P8_carriedOutAt = 1828
   P9_hasRank = 1829
   P10_hasAsDisciplinaryArea = 1830
   P1_isStudyAt = 1805
   P2_isTheStudyBy = 1806
   P3_wasObtainedBy = 1811
   P4_isObtentionOf = 1812
   P5_hasAcademicSupervisor = 1815
   P11_isDeliveredBy = 1831
   P12_isStudyOf = 1832
   P13_isObtainedAt = 1833
   P87_classifiesWith = 2932
   P88_classifies = 2933
   P1_takeCareOf = 1847
   P2_hasCaretaker = 1848
   P3_concernedPerson = 1849
   P4_concernedSchool = 1850
   P5_hasTakingCareType = 1855
   P6_hasAttendingASchoolType = 1856
   P34_isParticipationOnBehalfOf = 1642
   P57_isQualityInRelationTo = 1893
   P1_isReproductionOf = 1216
   P9_refersTo = 1334
   P18_hasDefinition = 1762
   P19_hasComment = 1763
   P20_hasValueVersion = 1864
   P21_hasTextType = 1865
   P22_hasCommentType = 1866
   P23_isAnnotatedIn = 1872
   P24_atPosition = 1874
   P25_annotatedEntity = 1875
   P26_mentions = 1876
   P27_isMentionedIn = 1877
   P28_atPosition = 1878
   P29_hasValue = 1879
   P30_isAbout = 1889
   P26_hasDatationValue = 2214
   P27_hasDatationType = 2272
   P31_hasMentioningContent = 2415
   P152_hasParent = 140
   P8_comprend = 1871
   P26_hasInformationObjectType = 1895
   P21_effectsDedication = 1922
   P22_hasDedicatoryObject = 1923
   P23_hasDedicatee = 1924
   P24_hasConceptualDedicatee = 1925
   P25_hasBeneficiary = 1926
   R66_includedPerformedVersionOf = 1039
   P58_isAbout = 1927
   P59_isQualityOf = 1928
   P61_isQualityOnBehalfOf = 1930
   P27_hasPerformanceType = 1931
   P19_hasActivityType = 1797
   P60_movedFrom = 2109
   P61_movedTo = 2110
   P62_displaces = 2111
   P29_hasMoveIdentifyingType = 2112
   P1_isMovementOf = 2116
   P2_hasMovementIdentifyingType = 2117
   P3_hasStopoverIdentifyingType = 2118
   P4_isJourneyOf = 2119
   P5_hasCarrierSJourneyIdentifyingType = 2120
   P6_isCoercedDisplacementOf = 2121
   P7_hasActorSCoercedTripIdentifyingType = 2122
   P8_isContinuationOf = 2123
   O9_observedPropertyType = 1075
   P30_observedEntityType = 2128
   P16_atDistance = 1183
   P57_isInsideOrRelativeTo = 1945
   P58_hasRelativeLocationType = 1946
   P59_isQualityOf = 1947
   P66_wasOrIsComposedOfObjectOfType = 2257
   P7_isIntentionOf = 1641
   P72_classifies = 2299
   P73_classifiesWith = 2300
   P64_hasTypeOfParticipation = 2274
   P28_plannedMoveFrom = 2312
   P29_plannedMoveTo = 2313
   P30_hasComponentDimension = 2314
   P31_hasQuantifiableComponentType = 2315
   P74_hasEpistemicSituationPreferredType = 2310
   P76_isQuantifiableQualityOf = 2316
   P77_isInvolvementIn = 2317
   P78_hasInvolvementType = 2318
   P79_isInvolvementOf = 2319
   P75_isQuantifiableQualityOf = 2311
   P80_isLinkedTo = 2320
   P81_hasLinkType = 2321
   P82_classifies = 2324
   P83_classifiesWith = 2325
   P65_hasParticipationRelationType = 2368
   P66_isParticipationRelationOf = 2369
   P67_isRoleIn = 2370
   P68_hasRoleQuality = 2371
   P34_hasContent = 1741
   P48_hasIntentionalExpressionIdentifyingType = 1800
   P89_isQuantifiableQualityOf = 2941
   P49_hasFormerOrCurrentKeeper = 45
   P50_hasCurrentKeeper = 46
   P51_hasFormerOrCurrentOwner = 47
   P71_lists = 62
   P92_broughtIntoExistence = 80
   P156_occupies = 141
   P157_isAtRestRelativeTo = 142
   O1_diminished = 1067
   O12_hasDimension = 1078
   O15_occupied = 1081
   P195_wasAPresenceOf = 1918
   P196_defines = 1919
   P198_holdsOrSupports = 1921
   O25_contains = 2113
   pc1_affects = 2327
   pc3_hasConnectionThrough = 2328
   pc4_showsBuildingFeature = 2329
   pc7_isConnectedThrough = 2332
   pc8_isConnectedTo = 2333
   pc10_belongsTo = 2335
   pc13_isRegulatedBy = 2338
   pc15_showsPlanConfigurationType = 2340
   pc16_showsStructuralSystem = 2341
   pc17_hasPerformanceEfficiencyDocumentedIn = 2342
   pc18_hasPhysicalRelationWith = 2343
   pc20_showsBuildingHomogeneityWith = 2347
   pc21_addressed = 2348
   pc21_1_hasType = 2349
   pc24_occurredIn = 2352
   pc25_occursIn = 2353
   pc26_isIllustratedBy = 2354
   pc30_resultedIn = 2358
   pc31_transformed = 2359
   pc42_wasEmbodiedBy = 2380
   pc67_showsAsConstructionComponent = 2873
   P86_isOfBiologicalObjectClassificationType = 2922
   P32_hasPropositionalObjectType = 2934

properties = PkProperty()

