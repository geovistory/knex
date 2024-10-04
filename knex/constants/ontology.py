from typing import List
from pydantic import BaseModel, Field

class OntoObject(BaseModel):
    pk: int
    label: str
    id: str

class Ontology(BaseModel):
    classes: List[OntoObject] = Field(default_factory=list)
    properties: List[OntoObject] = Field(default_factory=list)

    def klass(self, input: int | str) -> OntoObject:
        return self.__find(self.classes, input, 'class')

    def property(self, input: int | str) -> OntoObject:
        return self.__find(self.properties, input, 'property')

    def __find(self, ontoobjects: List[OntoObject], input: int | str, name=str) -> OntoObject:
        if isinstance(input, int): selection = [obj for obj in ontoobjects if input == obj.pk]
        elif isinstance(input, str): selection = [obj for obj in ontoobjects if input.lower() == obj.label.lower() or input.lower() == obj.id.lower()]
        else: raise Exception('Given input is neither a integer nor a string')

        if len(selection) == 0: raise Exception(f'Unknown ' + name + ' "' + input + '"')
        elif len(selection) == 1: return selection[0]
        else: raise Exception('Multiple ' + name + ' found with "' + input + '"')

ontology = Ontology()
ontology.classes.append(OntoObject(pk=7, label="Activity", id="E7"))
ontology.classes.append(OntoObject(pk=21, label="Person", id="E21"))
ontology.classes.append(OntoObject(pk=340, label="Physical Thing Life", id="C19"))
ontology.classes.append(OntoObject(pk=364, label="Geographical Place Type", id="C14"))
ontology.classes.append(OntoObject(pk=5, label="Event", id="E5"))
ontology.classes.append(OntoObject(pk=53, label="Type", id="E55"))
ontology.classes.append(OntoObject(pk=60, label="Formation", id="E66"))
ontology.classes.append(OntoObject(pk=62, label="Dissolution", id="E68"))
ontology.classes.append(OntoObject(pk=63, label="Death", id="E69"))
ontology.classes.append(OntoObject(pk=68, label="Group", id="E74"))
ontology.classes.append(OntoObject(pk=78, label="Joining", id="E85"))
ontology.classes.append(OntoObject(pk=79, label="Leaving", id="E86"))
ontology.classes.append(OntoObject(pk=212, label="Epistemic Location of a Physical Thing", id="C15"))
ontology.classes.append(OntoObject(pk=218, label="Expression", id="F2"))
ontology.classes.append(OntoObject(pk=220, label="Manifestation Singleton", id="F4"))
ontology.classes.append(OntoObject(pk=244, label="Expression Creation", id="F28"))
ontology.classes.append(OntoObject(pk=332, label="Activity Type", id="C3"))
ontology.classes.append(OntoObject(pk=363, label="Geographical Place", id="C13"))
ontology.classes.append(OntoObject(pk=441, label="Construction", id="C17"))
ontology.classes.append(OntoObject(pk=442, label="Membership", id="C5"))
ontology.classes.append(OntoObject(pk=443, label="Construction Type", id="C18"))
ontology.classes.append(OntoObject(pk=444, label="Actor's Social Quality", id="C2"))
ontology.classes.append(OntoObject(pk=449, label="Epistemic Location Type", id="C16"))
ontology.classes.append(OntoObject(pk=451, label="Group Type", id="C9"))
ontology.classes.append(OntoObject(pk=608, label="Membership Type", id="C6"))
ontology.classes.append(OntoObject(pk=717, label="Monetary amount", id="C21"))
ontology.classes.append(OntoObject(pk=718, label="Currency", id="C22"))
ontology.classes.append(OntoObject(pk=838, label="Event Type", id="C34"))
ontology.classes.append(OntoObject(pk=839, label="Location Reason", id="C35"))
ontology.classes.append(OntoObject(pk=969, label="Relative Location of a Physical Thing", id="C41"))
ontology.classes.append(OntoObject(pk=1, label="CRM Entity", id="E1"))
ontology.classes.append(OntoObject(pk=2, label="Temporal Entity", id="E2"))
ontology.classes.append(OntoObject(pk=32, label="Linguistic Object", id="E33"))
ontology.classes.append(OntoObject(pk=40, label="Appellation", id="E41"))
ontology.classes.append(OntoObject(pk=41, label="Identifier", id="E42"))
ontology.classes.append(OntoObject(pk=50, label="Time-Span", id="E52"))
ontology.classes.append(OntoObject(pk=51, label="Place", id="E53"))
ontology.classes.append(OntoObject(pk=54, label="Language", id="E56"))
ontology.classes.append(OntoObject(pk=71, label="Curated Holding", id="E78"))
ontology.classes.append(OntoObject(pk=84, label="Presence", id="E93"))
ontology.classes.append(OntoObject(pk=219, label="Manifestation Product Type", id="F3"))
ontology.classes.append(OntoObject(pk=221, label="Item", id="F5"))
ontology.classes.append(OntoObject(pk=234, label="Serial Work", id="F18"))
ontology.classes.append(OntoObject(pk=335, label="Time Primitive", id="E61"))
ontology.classes.append(OntoObject(pk=338, label="Number", id="E60"))
ontology.classes.append(OntoObject(pk=339, label="String", id="E62"))
ontology.classes.append(OntoObject(pk=365, label="Appellation in a Language", id="C11"))
ontology.classes.append(OntoObject(pk=445, label="Argument", id="C12"))
ontology.classes.append(OntoObject(pk=450, label="Manifestation Singleton Type", id="C10"))
ontology.classes.append(OntoObject(pk=452, label="Type of manifestation product type", id="C8"))
ontology.classes.append(OntoObject(pk=454, label="Expression Type", id="C6"))
ontology.classes.append(OntoObject(pk=455, label="[Geovistory] Digital", id="C1"))
ontology.classes.append(OntoObject(pk=456, label="Chunk", id="C2"))
ontology.classes.append(OntoObject(pk=457, label="Spot", id="C3"))
ontology.classes.append(OntoObject(pk=459, label="Argument's method", id="C13"))
ontology.classes.append(OntoObject(pk=502, label="Web Request", id="C4"))
ontology.classes.append(OntoObject(pk=503, label="Expression Portion", id="C2"))
ontology.classes.append(OntoObject(pk=516, label="Expression Portion Type", id="C3"))
ontology.classes.append(OntoObject(pk=518, label="Expression fragment", id="C6"))
ontology.classes.append(OntoObject(pk=519, label="Item Type", id="C5"))
ontology.classes.append(OntoObject(pk=520, label="Entity Quality Type", id="C20"))
ontology.classes.append(OntoObject(pk=521, label="Cell", id="C7"))
ontology.classes.append(OntoObject(pk=607, label="Web request type", id="C8"))
ontology.classes.append(OntoObject(pk=630, label="Appellation in a Language Type", id="C12"))
ontology.classes.append(OntoObject(pk=635, label="Tag", id="C9"))
ontology.classes.append(OntoObject(pk=657, label="Reference", id="C11"))
ontology.classes.append(OntoObject(pk=689, label="Duration", id="C1"))
ontology.classes.append(OntoObject(pk=690, label="Time unit", id="C2"))
ontology.classes.append(OntoObject(pk=698, label="Actor's Social Role", id="C12"))
ontology.classes.append(OntoObject(pk=707, label="Numeric dimension", id="C11"))
ontology.classes.append(OntoObject(pk=708, label="Numeric dimension type", id="C12"))
ontology.classes.append(OntoObject(pk=783, label="Uniform Resource Locator (URL)", id="C14"))
ontology.classes.append(OntoObject(pk=784, label="Short title", id="C15"))
ontology.classes.append(OntoObject(pk=785, label="Text", id="C16"))
ontology.classes.append(OntoObject(pk=827, label="Identifier Type", id="C24"))
ontology.classes.append(OntoObject(pk=867, label="Asserted Actor's Role", id="C9"))
ontology.classes.append(OntoObject(pk=868, label="Person Appellation in a Language", id="C38"))
ontology.classes.append(OntoObject(pk=869, label="Person Appellation in a Language Type", id="C39"))
ontology.classes.append(OntoObject(pk=870, label="Bibliographic Citation", id="C10"))
ontology.classes.append(OntoObject(pk=871, label="Citation Style", id="C11"))
ontology.classes.append(OntoObject(pk=872, label="Belonging to a Physical Collection", id="C27"))
ontology.classes.append(OntoObject(pk=873, label="Collection Type", id="C26"))
ontology.classes.append(OntoObject(pk=874, label="Manifestation Singleton Appellation Type", id="C17"))
ontology.classes.append(OntoObject(pk=967, label="Uniform Resource Identifier (URI)", id="C30"))
ontology.classes.append(OntoObject(pk=1076, label="Geographical Place Classification", id="C48"))
ontology.classes.append(OntoObject(pk=1210, label="Geographical Place Kind", id="C51"))
ontology.classes.append(OntoObject(pk=118, label="Naissance", id="TyIn14"))
ontology.classes.append(OntoObject(pk=128, label="Décès", id="TyIn26"))
ontology.classes.append(OntoObject(pk=134, label="Localisation", id="TyIn36"))
ontology.classes.append(OntoObject(pk=181, label="Obtenir une qualité", id="TyIn11"))
ontology.classes.append(OntoObject(pk=189, label="Passage d'un examen", id="TyIn145"))
ontology.classes.append(OntoObject(pk=191, label="Suspension d'activité", id="TyIn149"))
ontology.classes.append(OntoObject(pk=196, label="Création d'un acteur collectif", id="TyIn30"))
ontology.classes.append(OntoObject(pk=522, label="Ship", id="C2"))
ontology.classes.append(OntoObject(pk=523, label="Ship Voyage", id="C1"))
ontology.classes.append(OntoObject(pk=524, label="Ship Type", id="C3"))
ontology.classes.append(OntoObject(pk=525, label="Shipyard", id="C4"))
ontology.classes.append(OntoObject(pk=526, label="Economic good", id="C5"))
ontology.classes.append(OntoObject(pk=527, label="Transport", id="C6"))
ontology.classes.append(OntoObject(pk=528, label="Stopover", id="C7"))
ontology.classes.append(OntoObject(pk=529, label="VOC Chamber", id="C8"))
ontology.classes.append(OntoObject(pk=533, label="Shipbuilding", id="C12"))
ontology.classes.append(OntoObject(pk=535, label="Participation", id="C15"))
ontology.classes.append(OntoObject(pk=3, label="Condition State", id="E3"))
ontology.classes.append(OntoObject(pk=18, label="Physical Thing", id="E18"))
ontology.classes.append(OntoObject(pk=28, label="Design or Procedure", id="E29"))
ontology.classes.append(OntoObject(pk=30, label="Document", id="E31"))
ontology.classes.append(OntoObject(pk=34, label="Title", id="E35"))
ontology.classes.append(OntoObject(pk=38, label="Actor", id="E39"))
ontology.classes.append(OntoObject(pk=61, label="Birth", id="E67"))
ontology.classes.append(OntoObject(pk=64, label="Thing", id="E70"))
ontology.classes.append(OntoObject(pk=75, label="Actor Appellation", id="E82"))
ontology.classes.append(OntoObject(pk=81, label="Propositional Object", id="E89"))
ontology.classes.append(OntoObject(pk=556, label="Outcomes (external processes)", id="REO12"))
ontology.classes.append(OntoObject(pk=557, label="Disposition", id="REO2"))
ontology.classes.append(OntoObject(pk=558, label="Position", id="REO13"))
ontology.classes.append(OntoObject(pk=559, label="Environment", id="REO3"))
ontology.classes.append(OntoObject(pk=560, label="Location", id="REO9"))
ontology.classes.append(OntoObject(pk=561, label="Lighting", id="REO8"))
ontology.classes.append(OntoObject(pk=562, label="Circumstances", id="REO1"))
ontology.classes.append(OntoObject(pk=563, label="Intensity", id="REO7"))
ontology.classes.append(OntoObject(pk=564, label="Frequency", id="REO4"))
ontology.classes.append(OntoObject(pk=565, label="Nationality", id="REO10"))
ontology.classes.append(OntoObject(pk=566, label="Gender", id="REO5"))
ontology.classes.append(OntoObject(pk=567, label="Occupation", id="REO11"))
ontology.classes.append(OntoObject(pk=568, label="Religion (temporal entity)", id="REO15"))
ontology.classes.append(OntoObject(pk=569, label="Genre", id="REO6"))
ontology.classes.append(OntoObject(pk=570, label="Provenance", id="REO14"))
ontology.classes.append(OntoObject(pk=571, label="Status", id="REO16"))
ontology.classes.append(OntoObject(pk=629, label="Gender", id="C11"))
ontology.classes.append(OntoObject(pk=636, label="Occupation", id="C7"))
ontology.classes.append(OntoObject(pk=637, label="Occupation (Temporal entity)", id="C8"))
ontology.classes.append(OntoObject(pk=642, label="Habit", id="REO17"))
ontology.classes.append(OntoObject(pk=643, label="Aim", id="REO18"))
ontology.classes.append(OntoObject(pk=644, label="Skill", id="REO19"))
ontology.classes.append(OntoObject(pk=645, label="Understanding", id="REO20"))
ontology.classes.append(OntoObject(pk=646, label="Emotions", id="REO21"))
ontology.classes.append(OntoObject(pk=647, label="Evaluation", id="REO22"))
ontology.classes.append(OntoObject(pk=648, label="Effects (internal processes)", id="REO23"))
ontology.classes.append(OntoObject(pk=719, label="Skill", id="C21"))
ontology.classes.append(OntoObject(pk=755, label="Summary", id="REO26"))
ontology.classes.append(OntoObject(pk=789, label="Mental imagery", id="REO27"))
ontology.classes.append(OntoObject(pk=790, label="Memories (textual)", id="REO28"))
ontology.classes.append(OntoObject(pk=791, label="Memories (non textual)", id="REO29"))
ontology.classes.append(OntoObject(pk=792, label="Expectations", id="REO30"))
ontology.classes.append(OntoObject(pk=793, label="Action", id="REO31"))
ontology.classes.append(OntoObject(pk=794, label="Change in thinking", id="REO32"))
ontology.classes.append(OntoObject(pk=795, label="Output", id="REO33"))
ontology.classes.append(OntoObject(pk=797, label="Age (temporal entity)", id="REO35"))
ontology.classes.append(OntoObject(pk=798, label="Citizenship", id="REO36"))
ontology.classes.append(OntoObject(pk=799, label="Linguistic communities", id="REO37"))
ontology.classes.append(OntoObject(pk=800, label="Ethnic communities", id="REO38"))
ontology.classes.append(OntoObject(pk=801, label="Educational level", id="REO39"))
ontology.classes.append(OntoObject(pk=802, label="Subject matter", id="REO40"))
ontology.classes.append(OntoObject(pk=803, label="Medium", id="REO41"))
ontology.classes.append(OntoObject(pk=4, label="Period", id="E4"))
ontology.classes.append(OntoObject(pk=6, label="Destruction", id="E6"))
ontology.classes.append(OntoObject(pk=8, label="Acquisition", id="E8"))
ontology.classes.append(OntoObject(pk=9, label="Move", id="E9"))
ontology.classes.append(OntoObject(pk=10, label="Transfer of Custody", id="E10"))
ontology.classes.append(OntoObject(pk=11, label="Modification", id="E11"))
ontology.classes.append(OntoObject(pk=12, label="Production", id="E12"))
ontology.classes.append(OntoObject(pk=13, label="Attribute Assignment", id="E13"))
ontology.classes.append(OntoObject(pk=14, label="Condition Assessment", id="E14"))
ontology.classes.append(OntoObject(pk=15, label="Identifier Assignment", id="E15"))
ontology.classes.append(OntoObject(pk=16, label="Measurement", id="E16"))
ontology.classes.append(OntoObject(pk=17, label="Type Assignment", id="E17"))
ontology.classes.append(OntoObject(pk=19, label="Physical Object", id="E19"))
ontology.classes.append(OntoObject(pk=22, label="Human-Made Object", id="E22"))
ontology.classes.append(OntoObject(pk=23, label="Physical Human-Made Thing", id="E24"))
ontology.classes.append(OntoObject(pk=25, label="Physical Feature", id="E26"))
ontology.classes.append(OntoObject(pk=26, label="Site", id="E27"))
ontology.classes.append(OntoObject(pk=27, label="Conceptual Object", id="E28"))
ontology.classes.append(OntoObject(pk=29, label="Right", id="E30"))
ontology.classes.append(OntoObject(pk=31, label="Authority Document", id="E32"))
ontology.classes.append(OntoObject(pk=33, label="Inscription", id="E34"))
ontology.classes.append(OntoObject(pk=35, label="Visual Item", id="E36"))
ontology.classes.append(OntoObject(pk=36, label="Mark", id="E37"))
ontology.classes.append(OntoObject(pk=37, label="Image", id="E38"))
ontology.classes.append(OntoObject(pk=39, label="Legal Body", id="E40"))
ontology.classes.append(OntoObject(pk=42, label="Place Appellation", id="E44"))
ontology.classes.append(OntoObject(pk=43, label="Address", id="E45"))
ontology.classes.append(OntoObject(pk=44, label="Section Definition", id="E46"))
ontology.classes.append(OntoObject(pk=46, label="Place Name", id="E48"))
ontology.classes.append(OntoObject(pk=47, label="Time Appellation", id="E49"))
ontology.classes.append(OntoObject(pk=48, label="Date", id="E50"))
ontology.classes.append(OntoObject(pk=49, label="Contact Point", id="E51"))
ontology.classes.append(OntoObject(pk=52, label="Dimension", id="E54"))
ontology.classes.append(OntoObject(pk=55, label="Material", id="E57"))
ontology.classes.append(OntoObject(pk=56, label="Measurement Unit", id="E58"))
ontology.classes.append(OntoObject(pk=59, label="Creation", id="E65"))
ontology.classes.append(OntoObject(pk=65, label="Human-Made Thing", id="E71"))
ontology.classes.append(OntoObject(pk=67, label="Information Object", id="E73"))
ontology.classes.append(OntoObject(pk=69, label="Conceptual Object Appellation", id="E75"))
ontology.classes.append(OntoObject(pk=70, label="Persistent Item", id="E77"))
ontology.classes.append(OntoObject(pk=72, label="Part Addition", id="E79"))
ontology.classes.append(OntoObject(pk=73, label="Part Removal", id="E80"))
ontology.classes.append(OntoObject(pk=74, label="Transformation", id="E81"))
ontology.classes.append(OntoObject(pk=76, label="Type Creation", id="E83"))
ontology.classes.append(OntoObject(pk=80, label="Curation Activity", id="E87"))
ontology.classes.append(OntoObject(pk=82, label="Symbolic Object", id="E90"))
ontology.classes.append(OntoObject(pk=83, label="Spacetime Volume", id="E92"))
ontology.classes.append(OntoObject(pk=211, label="Entity Quality", id="C1"))
ontology.classes.append(OntoObject(pk=471, label="Belief", id="I2"))
ontology.classes.append(OntoObject(pk=472, label="Inference Logic", id="I3"))
ontology.classes.append(OntoObject(pk=473, label="Proposition Set", id="I4"))
ontology.classes.append(OntoObject(pk=474, label="Inference Making", id="I5"))
ontology.classes.append(OntoObject(pk=475, label="Belief Value", id="I6"))
ontology.classes.append(OntoObject(pk=572, label="Weaving", id="T1"))
ontology.classes.append(OntoObject(pk=573, label="Entering (Deprecated)", id="T2"))
ontology.classes.append(OntoObject(pk=574, label="Spinning (deprecated)", id="T3"))
ontology.classes.append(OntoObject(pk=575, label="Throwing (deprecated)", id="T4"))
ontology.classes.append(OntoObject(pk=576, label="Warping (deprecated)", id="T5"))
ontology.classes.append(OntoObject(pk=577, label="Loom", id="T6"))
ontology.classes.append(OntoObject(pk=578, label="Fabric", id="T7"))
ontology.classes.append(OntoObject(pk=579, label="Part Weaving", id="T8"))
ontology.classes.append(OntoObject(pk=580, label="Pattern Zone", id="T9"))
ontology.classes.append(OntoObject(pk=581, label="Ground", id="T10"))
ontology.classes.append(OntoObject(pk=582, label="Style", id="T11"))
ontology.classes.append(OntoObject(pk=583, label="Selvedge (deprecated)", id="T12"))
ontology.classes.append(OntoObject(pk=584, label="Style Assignment", id="T13"))
ontology.classes.append(OntoObject(pk=585, label="Starting Border (deprecated)", id="T14"))
ontology.classes.append(OntoObject(pk=586, label="Yarn", id="T15"))
ontology.classes.append(OntoObject(pk=587, label="Warp", id="T16"))
ontology.classes.append(OntoObject(pk=588, label="Weft", id="T17"))
ontology.classes.append(OntoObject(pk=589, label="Motif", id="T18"))
ontology.classes.append(OntoObject(pk=590, label="Object Domain Assignment", id="T19"))
ontology.classes.append(OntoObject(pk=591, label="Twist", id="T20"))
ontology.classes.append(OntoObject(pk=592, label="Weave", id="T21"))
ontology.classes.append(OntoObject(pk=594, label="Fabric Type", id="T23"))
ontology.classes.append(OntoObject(pk=595, label="Pattern Unit", id="T24"))
ontology.classes.append(OntoObject(pk=596, label="Weaving Technique", id="T25"))
ontology.classes.append(OntoObject(pk=597, label="Loom Type", id="T26"))
ontology.classes.append(OntoObject(pk=599, label="Yarn Type", id="T28"))
ontology.classes.append(OntoObject(pk=600, label="Twist Type", id="T29"))
ontology.classes.append(OntoObject(pk=601, label="Warp Type", id="T30"))
ontology.classes.append(OntoObject(pk=602, label="Warping Type (deprecated)", id="T31"))
ontology.classes.append(OntoObject(pk=603, label="Weave Type", id="T32"))
ontology.classes.append(OntoObject(pk=604, label="Weft Type", id="T33"))
ontology.classes.append(OntoObject(pk=605, label="Motif Type", id="T34"))
ontology.classes.append(OntoObject(pk=606, label="Object Type Assignment", id="T35"))
ontology.classes.append(OntoObject(pk=760, label="Quantifiable Quality", id="C28"))
ontology.classes.append(OntoObject(pk=832, label="Embroidery", id="T36"))
ontology.classes.append(OntoObject(pk=833, label="Galloon", id="T37"))
ontology.classes.append(OntoObject(pk=834, label="Lining", id="T38"))
ontology.classes.append(OntoObject(pk=633, label="Relationship", id="C9"))
ontology.classes.append(OntoObject(pk=634, label="Type of Persons' Interaction", id="C10"))
ontology.classes.append(OntoObject(pk=702, label="Persons' Interaction", id="C18"))
ontology.classes.append(OntoObject(pk=808, label="Legal Location of an Actor", id="C28"))
ontology.classes.append(OntoObject(pk=883, label="Legal Location Type", id="C33"))
ontology.classes.append(OntoObject(pk=384, label="Encounter Event", id="S19"))
ontology.classes.append(OntoObject(pk=727, label="Use", id="C23"))
ontology.classes.append(OntoObject(pk=728, label="Use type", id="C24"))
ontology.classes.append(OntoObject(pk=894, label="Physical Man-Made Thing Type", id="C2"))
ontology.classes.append(OntoObject(pk=213, label="Social Perception of an Actor", id="C1"))
ontology.classes.append(OntoObject(pk=631, label="Pre-matrimonial enquiry", id="C1"))
ontology.classes.append(OntoObject(pk=638, label="Marital status", id="C2"))
ontology.classes.append(OntoObject(pk=664, label="Pre-matrimonial enquiry motivation type", id="C3"))
ontology.classes.append(OntoObject(pk=691, label="Account of a journey or stay", id="C4"))
ontology.classes.append(OntoObject(pk=694, label="Concept referred to in a journey's or stay's account", id="C5"))
ontology.classes.append(OntoObject(pk=695, label="Frequency class", id="C6"))
ontology.classes.append(OntoObject(pk=334, label="Social Relationship", id="C3"))
ontology.classes.append(OntoObject(pk=632, label="Social Relationship Type", id="C4"))
ontology.classes.append(OntoObject(pk=1714, label="Actor's Role in a Social Relationship", id="C43"))
ontology.classes.append(OntoObject(pk=897, label="Activity Domain", id="C34"))
ontology.classes.append(OntoObject(pk=677, label="Physical Human-Made Thing Type", id="C4"))
ontology.classes.append(OntoObject(pk=709, label="Length", id="C13"))
ontology.classes.append(OntoObject(pk=710, label="Length measurement unit", id="C14"))
ontology.classes.append(OntoObject(pk=711, label="Weight", id="C15"))
ontology.classes.append(OntoObject(pk=712, label="Weight measurement unit", id="C16"))
ontology.classes.append(OntoObject(pk=713, label="Area", id="C17"))
ontology.classes.append(OntoObject(pk=714, label="Area measurement unit", id="C18"))
ontology.classes.append(OntoObject(pk=715, label="Volume measurement unit", id="C19"))
ontology.classes.append(OntoObject(pk=716, label="Volume", id="C20"))
ontology.classes.append(OntoObject(pk=726, label="Physical Component", id="C22"))
ontology.classes.append(OntoObject(pk=217, label="Work", id="F1"))
ontology.classes.append(OntoObject(pk=676, label="Expression Publication Event", id="C1"))
ontology.classes.append(OntoObject(pk=721, label="Procedure", id="C4"))
ontology.classes.append(OntoObject(pk=722, label="Step", id="C5"))
ontology.classes.append(OntoObject(pk=723, label="Component of a Recipe", id="C6"))
ontology.classes.append(OntoObject(pk=724, label="Procedure Type", id="C7"))
ontology.classes.append(OntoObject(pk=725, label="Step Type", id="C8"))
ontology.classes.append(OntoObject(pk=1290, label="General Technique", id="C53"))
ontology.classes.append(OntoObject(pk=1752, label="Expression Portion Classification", id="C18"))
ontology.classes.append(OntoObject(pk=1756, label="Subject", id="C19"))
ontology.classes.append(OntoObject(pk=688, label="Holding of a Right or Obligation", id="C14"))
ontology.classes.append(OntoObject(pk=697, label="Social Role Embodiment", id="C13"))
ontology.classes.append(OntoObject(pk=701, label="Custom or Law", id="C17"))
ontology.classes.append(OntoObject(pk=720, label="Legal Quality Type", id="C22"))
ontology.classes.append(OntoObject(pk=758, label="Religious Identity", id="C23"))
ontology.classes.append(OntoObject(pk=759, label="Religion or Religious Denomination", id="C24"))
ontology.classes.append(OntoObject(pk=786, label="Abstract individual", id="C32"))
ontology.classes.append(OntoObject(pk=787, label="Political or Administrative Entity", id="C25"))
ontology.classes.append(OntoObject(pk=806, label="Legal Quality", id="C26"))
ontology.classes.append(OntoObject(pk=807, label="Legal Fact", id="C27"))
ontology.classes.append(OntoObject(pk=847, label="Legal Quality Acquisition", id="C29"))
ontology.classes.append(OntoObject(pk=848, label="Actor's Legal Quality Acquisition Type", id="C30"))
ontology.classes.append(OntoObject(pk=866, label="Holding of a Right Type", id="C31"))
ontology.classes.append(OntoObject(pk=882, label="Social Role Type", id="C32"))
ontology.classes.append(OntoObject(pk=887, label="Intentional Event", id="C10"))
ontology.classes.append(OntoObject(pk=1491, label="Political or Administrative Entity Type", id="C42"))
ontology.classes.append(OntoObject(pk=704, label="Being in Force", id="C20"))
ontology.classes.append(OntoObject(pk=705, label="Custom or Law Type", id="C21"))
ontology.classes.append(OntoObject(pk=656, label="Namespace", id="C10"))
ontology.classes.append(OntoObject(pk=826, label="Identification", id="C23"))
ontology.classes.append(OntoObject(pk=388, label="Excavation Process Unit", id="A1"))
ontology.classes.append(OntoObject(pk=389, label="Stratigraphic Volume Unit", id="A2"))
ontology.classes.append(OntoObject(pk=390, label="Stratigraphic Interface", id="A3"))
ontology.classes.append(OntoObject(pk=394, label="Embedding", id="A7"))
ontology.classes.append(OntoObject(pk=396, label="Archaeological Excavation", id="A9"))
ontology.classes.append(OntoObject(pk=840, label="Archaeological Excavation Type", id="C1"))
ontology.classes.append(OntoObject(pk=841, label="Excavation Process Unit Type", id="C2"))
ontology.classes.append(OntoObject(pk=680, label="Built Work", id="B1"))
ontology.classes.append(OntoObject(pk=681, label="Morphological Building Section", id="B2"))
ontology.classes.append(OntoObject(pk=682, label="Filled Morphological Building Section", id="B3"))
ontology.classes.append(OntoObject(pk=683, label="Empty Morphological Building Section", id="B4"))
ontology.classes.append(OntoObject(pk=947, label="Dimension Type", id="C27"))
ontology.classes.append(OntoObject(pk=831, label="Teaching", id="C1"))
ontology.classes.append(OntoObject(pk=859, label="Academic Discipline", id="C5"))
ontology.classes.append(OntoObject(pk=860, label="Academic Chair", id="C6"))
ontology.classes.append(OntoObject(pk=861, label="Academic Position", id="C7"))
ontology.classes.append(OntoObject(pk=846, label="Study", id="C2"))
ontology.classes.append(OntoObject(pk=849, label="Obtaining a Study Title", id="C3"))
ontology.classes.append(OntoObject(pk=850, label="Study title", id="C4"))
ontology.classes.append(OntoObject(pk=1766, label="Group Classification", id="C70"))
ontology.classes.append(OntoObject(pk=879, label="Taking Care of a Person", id="C1"))
ontology.classes.append(OntoObject(pk=880, label="Attending a School", id="C2"))
ontology.classes.append(OntoObject(pk=884, label="Taking Care of a Person Type", id="C3"))
ontology.classes.append(OntoObject(pk=885, label="Attending a School Type", id="C4"))
ontology.classes.append(OntoObject(pk=946, label="Actor's Quality in Relation to an Event", id="C35"))
ontology.classes.append(OntoObject(pk=898, label="Table", id="C18"))
ontology.classes.append(OntoObject(pk=899, label="Definition", id="C19"))
ontology.classes.append(OntoObject(pk=900, label="Comment", id="C20"))
ontology.classes.append(OntoObject(pk=903, label="Text type", id="C23"))
ontology.classes.append(OntoObject(pk=904, label="Comment type", id="C24"))
ontology.classes.append(OntoObject(pk=933, label="Annotation in Text", id="C26"))
ontology.classes.append(OntoObject(pk=934, label="Annotation in Table", id="C27"))
ontology.classes.append(OntoObject(pk=935, label="Mentioning", id="C28"))
ontology.classes.append(OntoObject(pk=936, label="Table Value", id="C29"))
ontology.classes.append(OntoObject(pk=968, label="Mentioning in Table", id="C31"))
ontology.classes.append(OntoObject(pk=1150, label="Propositional Datation", id="C13"))
ontology.classes.append(OntoObject(pk=1295, label="Datation Type", id="C14"))
ontology.classes.append(OntoObject(pk=627, label="Building", id="Building"))
ontology.classes.append(OntoObject(pk=809, label="A1_Endurant", id="A1_Endurant"))
ontology.classes.append(OntoObject(pk=810, label="A3_Quality", id="A3_Quality"))
ontology.classes.append(OntoObject(pk=811, label="A2_Perdurant", id="A2_Perdurant"))
ontology.classes.append(OntoObject(pk=916, label="A22111_A-Procedure", id="A22111_A-Procedure"))
ontology.classes.append(OntoObject(pk=922, label="A2224_End_of_activity", id="A2224_End_of_activity"))
ontology.classes.append(OntoObject(pk=923, label="A2225_Patrimonalization", id="A2225_Patrimonalization"))
ontology.classes.append(OntoObject(pk=925, label="A0_Any_Artefact_Entity", id="A0_Any_Artefact_Entity"))
ontology.classes.append(OntoObject(pk=930, label="Glacière", id="C9"))
ontology.classes.append(OntoObject(pk=948, label="Information Object Type", id="C28"))
ontology.classes.append(OntoObject(pk=955, label="Dedication", id="C12"))
ontology.classes.append(OntoObject(pk=247, label="Performance", id="F31"))
ontology.classes.append(OntoObject(pk=956, label="Performance Type", id="C29"))
ontology.classes.append(OntoObject(pk=1063, label="Move Type", id="C31"))
ontology.classes.append(OntoObject(pk=1065, label="Actor's Movement or Journey", id="C1"))
ontology.classes.append(OntoObject(pk=1066, label="Stopover", id="C2"))
ontology.classes.append(OntoObject(pk=1067, label="Stopover Type", id="C3"))
ontology.classes.append(OntoObject(pk=1068, label="Actor's Movement or Journey Type", id="C4"))
ontology.classes.append(OntoObject(pk=1069, label="Carrier's Journey", id="C5"))
ontology.classes.append(OntoObject(pk=1070, label="Carrier's Journey Type", id="C6"))
ontology.classes.append(OntoObject(pk=1071, label="Actor's Coerced Trip", id="C7"))
ontology.classes.append(OntoObject(pk=1072, label="Actor's Coerced Trip Type", id="C8"))
ontology.classes.append(OntoObject(pk=369, label="Observation", id="S4"))
ontology.classes.append(OntoObject(pk=374, label="Property Type", id="S9"))
ontology.classes.append(OntoObject(pk=1077, label="Observed Entity Type", id="C32"))
ontology.classes.append(OntoObject(pk=971, label="Relative Location Type", id="C43"))
ontology.classes.append(OntoObject(pk=1152, label="Amount of Matter", id="C49"))
ontology.classes.append(OntoObject(pk=1289, label="Physical Set", id="C52"))
ontology.classes.append(OntoObject(pk=752, label="Intentional Collective", id="C25"))
ontology.classes.append(OntoObject(pk=881, label="Intentional Entity", id="C9"))
ontology.classes.append(OntoObject(pk=1361, label="Physical Human-Made Thing Classification", id="C55"))
ontology.classes.append(OntoObject(pk=1296, label="Participation Type", id="C36"))
ontology.classes.append(OntoObject(pk=1373, label="Planned Move", id="C15"))
ontology.classes.append(OntoObject(pk=1374, label="Quantifiable Component", id="C16"))
ontology.classes.append(OntoObject(pk=1375, label="Quantifiable Component Type", id="C17"))
ontology.classes.append(OntoObject(pk=696, label="Epistemic Situation", id="C3"))
ontology.classes.append(OntoObject(pk=1371, label="Epistemic Situation Type", id="C56"))
ontology.classes.append(OntoObject(pk=1377, label="Quantifiable Quality of an Epistemic Situation", id="C59"))
ontology.classes.append(OntoObject(pk=1378, label="Thing Involved in an Epistemic Situation", id="C60"))
ontology.classes.append(OntoObject(pk=1379, label="Type of Involvement of a Thing in an Epistemic Situation", id="C61"))
ontology.classes.append(OntoObject(pk=1372, label="Quantifiable Quality of a Spatio-Temporal Phenomenon", id="C57"))
ontology.classes.append(OntoObject(pk=1380, label="Link", id="C62"))
ontology.classes.append(OntoObject(pk=1381, label="Link Type", id="C63"))
ontology.classes.append(OntoObject(pk=1383, label="Purpose", id="C34"))
ontology.classes.append(OntoObject(pk=1384, label="Event Classification", id="C64"))
ontology.classes.append(OntoObject(pk=1385, label="Event Classification Type", id="C65"))
ontology.classes.append(OntoObject(pk=973, label="Physical Displacement", id="C45"))
ontology.classes.append(OntoObject(pk=1431, label="Participation Relation", id="C39"))
ontology.classes.append(OntoObject(pk=1432, label="Participation Relation Type", id="C40"))
ontology.classes.append(OntoObject(pk=1433, label="Role in Participation Relation", id="C41"))
ontology.classes.append(OntoObject(pk=1062, label="Intentional Expression", id="C46"))
ontology.classes.append(OntoObject(pk=1064, label="Intentional Expression Type", id="C47"))
ontology.classes.append(OntoObject(pk=1775, label="Quantifiable Quality of an Intentional Event", id="C71"))
ontology.classes.append(OntoObject(pk=1781, label="Quantifiable Quality of an Intentional Event Type", id="C72"))
ontology.classes.append(OntoObject(pk=57, label="Beginning of Existence", id="E63"))
ontology.classes.append(OntoObject(pk=58, label="End of Existence", id="E64"))
ontology.classes.append(OntoObject(pk=336, label="Space Primitive", id="E94"))
ontology.classes.append(OntoObject(pk=366, label="Matter Removal", id="S1"))
ontology.classes.append(OntoObject(pk=375, label="Material Substantial", id="S10"))
ontology.classes.append(OntoObject(pk=380, label="Observable Entity", id="S15"))
ontology.classes.append(OntoObject(pk=1386, label="Built Entity", id="CP1"))
ontology.classes.append(OntoObject(pk=1387, label="Architecture work", id="CP2"))
ontology.classes.append(OntoObject(pk=1388, label="Construction Unit", id="CP3"))
ontology.classes.append(OntoObject(pk=1389, label="Construction Component", id="CP4"))
ontology.classes.append(OntoObject(pk=1390, label="Construction Element Plural", id="CP5"))
ontology.classes.append(OntoObject(pk=1391, label="Construction Element Singular", id="CP6"))
ontology.classes.append(OntoObject(pk=1392, label="Architecture Decoration", id="CP7"))
ontology.classes.append(OntoObject(pk=1393, label="Equipment", id="CP8"))
ontology.classes.append(OntoObject(pk=1394, label="Building Material", id="CP9"))
ontology.classes.append(OntoObject(pk=1395, label="Building Unit", id="CP10"))
ontology.classes.append(OntoObject(pk=1396, label="Building Front", id="CP11"))
ontology.classes.append(OntoObject(pk=1397, label="Building Floor", id="CP12"))
ontology.classes.append(OntoObject(pk=1398, label="Urban Unit", id="CP13"))
ontology.classes.append(OntoObject(pk=1401, label="Urban Unit Front", id="CP14"))
ontology.classes.append(OntoObject(pk=1402, label="Open Air Area", id="CP15"))
ontology.classes.append(OntoObject(pk=1403, label="Urban Area", id="CP16"))
ontology.classes.append(OntoObject(pk=1404, label="Landscape Element", id="CP17"))
ontology.classes.append(OntoObject(pk=1405, label="Space Entity", id="CP18"))
ontology.classes.append(OntoObject(pk=1406, label="Historic Centre", id="CP19"))
ontology.classes.append(OntoObject(pk=1407, label="Construction Work", id="CP20"))
ontology.classes.append(OntoObject(pk=1408, label="Space Unit", id="CP21"))
ontology.classes.append(OntoObject(pk=1409, label="Space Component", id="CP22"))
ontology.classes.append(OntoObject(pk=1410, label="Maintenance", id="CP23"))
ontology.classes.append(OntoObject(pk=1411, label="Architecture Conservation Project Activity", id="CP24"))
ontology.classes.append(OntoObject(pk=1412, label="Conservation Intervention", id="CP25"))
ontology.classes.append(OntoObject(pk=1413, label="Typological Variation", id="CP26"))
ontology.classes.append(OntoObject(pk=1414, label="Architecture Analysis Output", id="CP27"))
ontology.classes.append(OntoObject(pk=1415, label="Building Feature", id="CP28"))
ontology.classes.append(OntoObject(pk=1416, label="Building Phase", id="CP29"))
ontology.classes.append(OntoObject(pk=1417, label="Architecture Condition Assessment", id="CP30"))
ontology.classes.append(OntoObject(pk=1418, label="Mechanical Damage Assessment", id="CP31"))
ontology.classes.append(OntoObject(pk=1419, label="Architecture Features Analysis", id="CP32"))
ontology.classes.append(OntoObject(pk=1420, label="Architecture Conservation Project", id="CP33"))
ontology.classes.append(OntoObject(pk=1421, label="Architecture Depiction", id="CP34"))
ontology.classes.append(OntoObject(pk=1422, label="Building-Formal Type", id="CP35"))
ontology.classes.append(OntoObject(pk=1423, label="Architecture Type", id="CP36"))
ontology.classes.append(OntoObject(pk=1424, label="Architecture Graphic Representation Type", id="CP37"))
ontology.classes.append(OntoObject(pk=1425, label="Architecture Representation Object", id="CP38"))
ontology.classes.append(OntoObject(pk=1426, label="Architecture Alpha-Numeric Representation Type", id="CP39"))
ontology.classes.append(OntoObject(pk=1427, label="Historic Centre", id="CP40"))
ontology.classes.append(OntoObject(pk=1703, label="Environmental Observable Entity", id="CP41"))
ontology.classes.append(OntoObject(pk=1704, label="Construction Site", id="CP44"))
ontology.classes.append(OntoObject(pk=1705, label="Material Decay", id="CP42"))
ontology.classes.append(OntoObject(pk=1706, label="Structural Damage", id="CP43"))
ontology.classes.append(OntoObject(pk=1707, label="Architecture Project", id="CP45"))
ontology.classes.append(OntoObject(pk=1708, label="Building Activity", id="CP46"))
ontology.classes.append(OntoObject(pk=1715, label="Urban Plan", id="CP49"))
ontology.classes.append(OntoObject(pk=1753, label="Animal", id="C67"))
ontology.classes.append(OntoObject(pk=1754, label="Biological Object Classification Type", id="C68"))
ontology.classes.append(OntoObject(pk=1768, label="Propositional Object Type", id="C35"))
ontology.classes.append(OntoObject(pk=1357, label="Economic Transaction", id="C37"))
ontology.classes.append(OntoObject(pk=1359, label="Presence of a Thing", id="C38"))
ontology.classes.append(OntoObject(pk=1811, label="Presence of a Thing Type", id="C44"))
ontology.classes.append(OntoObject(pk=1812, label="Economic Transaction Type", id="C45"))

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
   C27_dimensionType = 947
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
   C34_purpose = 1383
   C64_eventClassification = 1384
   C65_eventClassificationType = 1385
   C45_physicalDisplacement = 973
   C39_participationRelation = 1431
   C40_participationRelationType = 1432
   C41_roleInParticipationRelation = 1433
   C46_intentionalExpression = 1062
   C47_intentionalExpressionType = 1064
   C71_quantifiableQualityOfAnIntentionalEvent = 1775
   C72_quantifiableQualityOfAnIntentionalEventType = 1781
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
   CP17_landscapeElement = 1404
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
   C37_economicTransaction = 1357
   C38_presenceOfAThing = 1359
   C44_presenceOfAThingType = 1811
   C45_economicTransactionType = 1812
classes = PkClass()

ontology.properties.append(OntoObject(pk=7, label="took place on or within", id="P8"))
ontology.properties.append(OntoObject(pk=83, label="has formed", id="P95"))
ontology.properties.append(OntoObject(pk=87, label="dissolved", id="P99"))
ontology.properties.append(OntoObject(pk=88, label="was death of", id="P100"))
ontology.properties.append(OntoObject(pk=107, label="meets in time with", id="P119"))
ontology.properties.append(OntoObject(pk=108, label="occurs before", id="P120"))
ontology.properties.append(OntoObject(pk=115, label="has broader term", id="P127"))
ontology.properties.append(OntoObject(pk=131, label="joined", id="P143"))
ontology.properties.append(OntoObject(pk=132, label="joined with", id="P144"))
ontology.properties.append(OntoObject(pk=133, label="separated", id="P145"))
ontology.properties.append(OntoObject(pk=134, label="separated from", id="P146"))
ontology.properties.append(OntoObject(pk=139, label="was formed from", id="P151"))
ontology.properties.append(OntoObject(pk=991, label="created", id="R17"))
ontology.properties.append(OntoObject(pk=992, label="created", id="R18"))
ontology.properties.append(OntoObject(pk=1066, label="has location type", id="P19"))
ontology.properties.append(OntoObject(pk=1177, label="is location of", id="P17"))
ontology.properties.append(OntoObject(pk=1178, label="is location at", id="P15"))
ontology.properties.append(OntoObject(pk=1188, label="was a membership of", id="P1"))
ontology.properties.append(OntoObject(pk=1189, label="was membership in", id="P2"))
ontology.properties.append(OntoObject(pk=1190, label="has construction type", id="P9"))
ontology.properties.append(OntoObject(pk=1203, label="has event type", id="P47"))
ontology.properties.append(OntoObject(pk=1204, label="has group type", id="P7"))
ontology.properties.append(OntoObject(pk=1357, label="is part of", id="P5"))
ontology.properties.append(OntoObject(pk=1413, label="has membership type", id="P3"))
ontology.properties.append(OntoObject(pk=1640, label="has currency", id="P16"))
ontology.properties.append(OntoObject(pk=1798, label="has location reason", id="P46"))
ontology.properties.append(OntoObject(pk=1, label="is identified by", id="P1"))
ontology.properties.append(OntoObject(pk=4, label="has time-span", id="P4"))
ontology.properties.append(OntoObject(pk=63, label="has language", id="P72"))
ontology.properties.append(OntoObject(pk=71, label="ongoing throughout", id="P81"))
ontology.properties.append(OntoObject(pk=72, label="at some time within", id="P82"))
ontology.properties.append(OntoObject(pk=78, label="has value", id="P90"))
ontology.properties.append(OntoObject(pk=145, label="is temporally specified by", id="P164"))
ontology.properties.append(OntoObject(pk=146, label="incorporates", id="P165"))
ontology.properties.append(OntoObject(pk=147, label="was a presence of", id="P166"))
ontology.properties.append(OntoObject(pk=148, label="was within", id="P167"))
ontology.properties.append(OntoObject(pk=150, label="end of the begin", id="P81a"))
ontology.properties.append(OntoObject(pk=151, label="begin of the end", id="P81b"))
ontology.properties.append(OntoObject(pk=152, label="begin of the begin", id="P82a"))
ontology.properties.append(OntoObject(pk=153, label="end of the end", id="P82b"))
ontology.properties.append(OntoObject(pk=979, label="carriers provided by", id="R4"))
ontology.properties.append(OntoObject(pk=982, label="is example of", id="R7"))
ontology.properties.append(OntoObject(pk=1016, label="is representative manifestation singleton for", id="R42"))
ontology.properties.append(OntoObject(pk=1110, label="has geographical place kind", id="P20"))
ontology.properties.append(OntoObject(pk=1111, label="is appellation for language of", id="P11"))
ontology.properties.append(OntoObject(pk=1112, label="used in language", id="P12"))
ontology.properties.append(OntoObject(pk=1113, label="refers to name", id="P13"))
ontology.properties.append(OntoObject(pk=1205, label="has manifestation singleton type", id="P6"))
ontology.properties.append(OntoObject(pk=1206, label="has type of manifestation product type", id="P5"))
ontology.properties.append(OntoObject(pk=1214, label="has expression type", id="P4"))
ontology.properties.append(OntoObject(pk=1246, label="has argument method", id="P15"))
ontology.properties.append(OntoObject(pk=1305, label="is server response to request", id="P4"))
ontology.properties.append(OntoObject(pk=1316, label="has carrier provided by", id="P5"))
ontology.properties.append(OntoObject(pk=1317, label="is part of", id="P4"))
ontology.properties.append(OntoObject(pk=1320, label="has expression portion type", id="P5"))
ontology.properties.append(OntoObject(pk=1321, label="has item type", id="P2"))
ontology.properties.append(OntoObject(pk=1323, label="has web request type", id="P8"))
ontology.properties.append(OntoObject(pk=1430, label="has appellation for language type", id="P14"))
ontology.properties.append(OntoObject(pk=1440, label="tagged by", id="P12"))
ontology.properties.append(OntoObject(pk=1499, label="should be merged with", id="P13"))
ontology.properties.append(OntoObject(pk=1612, label="has time unit", id="P10"))
ontology.properties.append(OntoObject(pk=1635, label="has numeric dimension type", id="P11"))
ontology.properties.append(OntoObject(pk=1760, label="has web address", id="P16"))
ontology.properties.append(OntoObject(pk=1761, label="has short title", id="P17"))
ontology.properties.append(OntoObject(pk=1783, label="has identifier type", id="P19"))
ontology.properties.append(OntoObject(pk=1837, label="is role of", id="P15"))
ontology.properties.append(OntoObject(pk=1838, label="is asserted by", id="P16"))
ontology.properties.append(OntoObject(pk=1839, label="is qualified by", id="P17"))
ontology.properties.append(OntoObject(pk=1840, label="is in the role of", id="P18"))
ontology.properties.append(OntoObject(pk=1841, label="has style", id="P19"))
ontology.properties.append(OntoObject(pk=1842, label="same as external identifier", id="P20"))
ontology.properties.append(OntoObject(pk=1843, label="has value", id="P21"))
ontology.properties.append(OntoObject(pk=1844, label="is about", id="P55"))
ontology.properties.append(OntoObject(pk=1845, label="belongs to", id="P56"))
ontology.properties.append(OntoObject(pk=1846, label="has preferred type", id="P63"))
ontology.properties.append(OntoObject(pk=1887, label="has issue", id="P20"))
ontology.properties.append(OntoObject(pk=1943, label="same as URI [owl:sameAs]", id="P28"))
ontology.properties.append(OntoObject(pk=2124, label="classifies", id="P68"))
ontology.properties.append(OntoObject(pk=2125, label="classifies with", id="P64"))
ontology.properties.append(OntoObject(pk=2283, label="could be the same entity as", id="P71"))
ontology.properties.append(OntoObject(pk=2899, label="has main language", id="P32"))
ontology.properties.append(OntoObject(pk=1335, label="had departure place", id="P1"))
ontology.properties.append(OntoObject(pk=1336, label="had arrival place", id="P2"))
ontology.properties.append(OntoObject(pk=1337, label="has ship type", id="P6"))
ontology.properties.append(OntoObject(pk=1338, label="was carried out by", id="P3"))
ontology.properties.append(OntoObject(pk=1339, label="took place at", id="P4"))
ontology.properties.append(OntoObject(pk=1340, label="was part of", id="P5"))
ontology.properties.append(OntoObject(pk=1341, label="has built", id="P7"))
ontology.properties.append(OntoObject(pk=1342, label="carried out by", id="P8"))
ontology.properties.append(OntoObject(pk=1343, label="is carried out in the context of", id="P9"))
ontology.properties.append(OntoObject(pk=1345, label="is participation in", id="P11"))
ontology.properties.append(OntoObject(pk=1354, label="has set up", id="P10"))
ontology.properties.append(OntoObject(pk=1358, label="carried", id="P11"))
ontology.properties.append(OntoObject(pk=1359, label="participated in", id="P12"))
ontology.properties.append(OntoObject(pk=2, label="has type", id="P2"))
ontology.properties.append(OntoObject(pk=6, label="took place at", id="P7"))
ontology.properties.append(OntoObject(pk=11, label="occurred in the presence of", id="P12"))
ontology.properties.append(OntoObject(pk=13, label="carried out by", id="P14"))
ontology.properties.append(OntoObject(pk=14, label="was influenced by", id="P15"))
ontology.properties.append(OntoObject(pk=15, label="used specific object", id="P16"))
ontology.properties.append(OntoObject(pk=31, label="used specific technique", id="P33"))
ontology.properties.append(OntoObject(pk=41, label="has condition", id="P44"))
ontology.properties.append(OntoObject(pk=43, label="is composed of", id="P46"))
ontology.properties.append(OntoObject(pk=44, label="has preferred identifier", id="P48"))
ontology.properties.append(OntoObject(pk=58, label="refers to", id="P67"))
ontology.properties.append(OntoObject(pk=61, label="documents", id="P70"))
ontology.properties.append(OntoObject(pk=86, label="brought into life", id="P98"))
ontology.properties.append(OntoObject(pk=90, label="has title", id="P102"))
ontology.properties.append(OntoObject(pk=117, label="is about", id="P129"))
ontology.properties.append(OntoObject(pk=119, label="is identified by", id="P131"))
ontology.properties.append(OntoObject(pk=122, label="continued", id="P134"))
ontology.properties.append(OntoObject(pk=1378, label="has occupation", id="readP1"))
ontology.properties.append(OntoObject(pk=1379, label="is nationality of", id="readP2"))
ontology.properties.append(OntoObject(pk=1380, label="has gender", id="readP3"))
ontology.properties.append(OntoObject(pk=1381, label="is religion of", id="readP4"))
ontology.properties.append(OntoObject(pk=1382, label="is genre of", id="readP5"))
ontology.properties.append(OntoObject(pk=1383, label="is provenance of", id="readP6"))
ontology.properties.append(OntoObject(pk=1384, label="is status of", id="readP7"))
ontology.properties.append(OntoObject(pk=1385, label="is frequency of", id="readP8"))
ontology.properties.append(OntoObject(pk=1386, label="is intensity of", id="readP9"))
ontology.properties.append(OntoObject(pk=1415, label="is outcome of", id="readP10"))
ontology.properties.append(OntoObject(pk=1429, label="has gender", id="P23"))
ontology.properties.append(OntoObject(pk=1441, label="is occupation of", id="P4"))
ontology.properties.append(OntoObject(pk=1442, label="is about", id="P5"))
ontology.properties.append(OntoObject(pk=1453, label="is disposition of", id="readP11"))
ontology.properties.append(OntoObject(pk=1454, label="is habit of", id="readP12"))
ontology.properties.append(OntoObject(pk=1455, label="is skill of", id="readP13"))
ontology.properties.append(OntoObject(pk=1493, label="precedes", id="readP14"))
ontology.properties.append(OntoObject(pk=1494, label="is aim of", id="readP15"))
ontology.properties.append(OntoObject(pk=1496, label="is part of", id="readP17"))
ontology.properties.append(OntoObject(pk=1747, label="has skill", id="P38"))
ontology.properties.append(OntoObject(pk=1768, label="is age of", id="readP21"))
ontology.properties.append(OntoObject(pk=1769, label="is citizenship of", id="readP22"))
ontology.properties.append(OntoObject(pk=1770, label="is educational level of", id="readP23"))
ontology.properties.append(OntoObject(pk=1771, label="is member of", id="readP24"))
ontology.properties.append(OntoObject(pk=1772, label="is member of", id="readP25"))
ontology.properties.append(OntoObject(pk=1773, label="is medium of", id="readP26"))
ontology.properties.append(OntoObject(pk=1775, label="is triggered by", id="readP27"))
ontology.properties.append(OntoObject(pk=1776, label="is triggered by", id="readP28"))
ontology.properties.append(OntoObject(pk=3, label="has note", id="P3"))
ontology.properties.append(OntoObject(pk=5, label="consists of", id="P5"))
ontology.properties.append(OntoObject(pk=8, label="consists of", id="P9"))
ontology.properties.append(OntoObject(pk=9, label="falls within", id="P10"))
ontology.properties.append(OntoObject(pk=10, label="had participant", id="P11"))
ontology.properties.append(OntoObject(pk=12, label="destroyed", id="P13"))
ontology.properties.append(OntoObject(pk=16, label="was motivated by", id="P17"))
ontology.properties.append(OntoObject(pk=17, label="was intended use of", id="P19"))
ontology.properties.append(OntoObject(pk=18, label="had specific purpose", id="P20"))
ontology.properties.append(OntoObject(pk=19, label="had general purpose", id="P21"))
ontology.properties.append(OntoObject(pk=20, label="transferred title to", id="P22"))
ontology.properties.append(OntoObject(pk=21, label="transferred title from", id="P23"))
ontology.properties.append(OntoObject(pk=22, label="transferred title of", id="P24"))
ontology.properties.append(OntoObject(pk=23, label="moved", id="P25"))
ontology.properties.append(OntoObject(pk=24, label="moved to", id="P26"))
ontology.properties.append(OntoObject(pk=25, label="moved from", id="P27"))
ontology.properties.append(OntoObject(pk=26, label="custody surrendered by", id="P28"))
ontology.properties.append(OntoObject(pk=27, label="custody received by", id="P29"))
ontology.properties.append(OntoObject(pk=28, label="transferred custody of", id="P30"))
ontology.properties.append(OntoObject(pk=29, label="has modified", id="P31"))
ontology.properties.append(OntoObject(pk=30, label="used general technique", id="P32"))
ontology.properties.append(OntoObject(pk=32, label="concerned", id="P34"))
ontology.properties.append(OntoObject(pk=33, label="has identified", id="P35"))
ontology.properties.append(OntoObject(pk=34, label="assigned", id="P37"))
ontology.properties.append(OntoObject(pk=35, label="deassigned", id="P38"))
ontology.properties.append(OntoObject(pk=36, label="measured", id="P39"))
ontology.properties.append(OntoObject(pk=37, label="observed dimension", id="P40"))
ontology.properties.append(OntoObject(pk=38, label="classified", id="P41"))
ontology.properties.append(OntoObject(pk=39, label="assigned", id="P42"))
ontology.properties.append(OntoObject(pk=40, label="has dimension", id="P43"))
ontology.properties.append(OntoObject(pk=42, label="consists of", id="P45"))
ontology.properties.append(OntoObject(pk=48, label="has current owner", id="P52"))
ontology.properties.append(OntoObject(pk=49, label="has former or current location", id="P53"))
ontology.properties.append(OntoObject(pk=51, label="has current location", id="P55"))
ontology.properties.append(OntoObject(pk=52, label="bears feature", id="P56"))
ontology.properties.append(OntoObject(pk=54, label="has section definition", id="P58"))
ontology.properties.append(OntoObject(pk=55, label="has section", id="P59"))
ontology.properties.append(OntoObject(pk=56, label="depicts", id="P62"))
ontology.properties.append(OntoObject(pk=57, label="shows visual item", id="P65"))
ontology.properties.append(OntoObject(pk=59, label="foresees use of", id="P68"))
ontology.properties.append(OntoObject(pk=60, label="has association with", id="P69"))
ontology.properties.append(OntoObject(pk=64, label="has translation", id="P73"))
ontology.properties.append(OntoObject(pk=66, label="possesses", id="P75"))
ontology.properties.append(OntoObject(pk=67, label="has contact point", id="P76"))
ontology.properties.append(OntoObject(pk=68, label="is identified by", id="P78"))
ontology.properties.append(OntoObject(pk=69, label="beginning is qualified by", id="P79"))
ontology.properties.append(OntoObject(pk=70, label="end is qualified by", id="P80"))
ontology.properties.append(OntoObject(pk=73, label="had at least duration", id="P83"))
ontology.properties.append(OntoObject(pk=74, label="had at most duration", id="P84"))
ontology.properties.append(OntoObject(pk=75, label="falls within", id="P86"))
ontology.properties.append(OntoObject(pk=76, label="is identified by", id="P87"))
ontology.properties.append(OntoObject(pk=77, label="falls within", id="P89"))
ontology.properties.append(OntoObject(pk=79, label="has unit", id="P91"))
ontology.properties.append(OntoObject(pk=81, label="took out of existence", id="P93"))
ontology.properties.append(OntoObject(pk=82, label="has created", id="P94"))
ontology.properties.append(OntoObject(pk=84, label="by mother", id="P96"))
ontology.properties.append(OntoObject(pk=85, label="from father", id="P97"))
ontology.properties.append(OntoObject(pk=89, label="had as general use", id="P101"))
ontology.properties.append(OntoObject(pk=91, label="was intended for", id="P103"))
ontology.properties.append(OntoObject(pk=92, label="is subject to", id="P104"))
ontology.properties.append(OntoObject(pk=93, label="right held by", id="P105"))
ontology.properties.append(OntoObject(pk=94, label="is composed of", id="P106"))
ontology.properties.append(OntoObject(pk=95, label="has current or former member", id="P107"))
ontology.properties.append(OntoObject(pk=96, label="has produced", id="P108"))
ontology.properties.append(OntoObject(pk=98, label="augmented", id="P110"))
ontology.properties.append(OntoObject(pk=99, label="added", id="P111"))
ontology.properties.append(OntoObject(pk=100, label="diminished", id="P112"))
ontology.properties.append(OntoObject(pk=101, label="removed", id="P113"))
ontology.properties.append(OntoObject(pk=102, label="is equal in time to", id="P114"))
ontology.properties.append(OntoObject(pk=103, label="finishes", id="P115"))
ontology.properties.append(OntoObject(pk=104, label="starts", id="P116"))
ontology.properties.append(OntoObject(pk=105, label="occurs during", id="P117"))
ontology.properties.append(OntoObject(pk=106, label="overlaps in time with", id="P118"))
ontology.properties.append(OntoObject(pk=109, label="overlaps with", id="P121"))
ontology.properties.append(OntoObject(pk=110, label="borders with", id="P122"))
ontology.properties.append(OntoObject(pk=111, label="resulted in", id="P123"))
ontology.properties.append(OntoObject(pk=112, label="transformed", id="P124"))
ontology.properties.append(OntoObject(pk=113, label="used object of type", id="P125"))
ontology.properties.append(OntoObject(pk=114, label="employed", id="P126"))
ontology.properties.append(OntoObject(pk=116, label="carries", id="P128"))
ontology.properties.append(OntoObject(pk=118, label="shows features of", id="P130"))
ontology.properties.append(OntoObject(pk=123, label="created type", id="P135"))
ontology.properties.append(OntoObject(pk=124, label="was based on", id="P136"))
ontology.properties.append(OntoObject(pk=125, label="exemplifies", id="P137"))
ontology.properties.append(OntoObject(pk=126, label="represents", id="P138"))
ontology.properties.append(OntoObject(pk=127, label="has alternative form", id="P139"))
ontology.properties.append(OntoObject(pk=128, label="assigned attribute to", id="P140"))
ontology.properties.append(OntoObject(pk=129, label="assigned", id="P141"))
ontology.properties.append(OntoObject(pk=130, label="used constituent", id="P142"))
ontology.properties.append(OntoObject(pk=135, label="curated", id="P147"))
ontology.properties.append(OntoObject(pk=136, label="has component", id="P148"))
ontology.properties.append(OntoObject(pk=137, label="is identified by", id="P149"))
ontology.properties.append(OntoObject(pk=1042, label="has quantifiable quality", id="P22"))
ontology.properties.append(OntoObject(pk=1247, label="used as premise", id="J1"))
ontology.properties.append(OntoObject(pk=1248, label="concluded that", id="J2"))
ontology.properties.append(OntoObject(pk=1249, label="applies", id="J3"))
ontology.properties.append(OntoObject(pk=1250, label="that", id="J4"))
ontology.properties.append(OntoObject(pk=1251, label="holds to be", id="J5"))
ontology.properties.append(OntoObject(pk=1394, label="assigned object type", id="L1"))
ontology.properties.append(OntoObject(pk=1396, label="has yarn type", id="L3"))
ontology.properties.append(OntoObject(pk=1397, label="assigned domain type", id="L4"))
ontology.properties.append(OntoObject(pk=1398, label="has twist type", id="L5"))
ontology.properties.append(OntoObject(pk=1399, label="has warp type", id="L6"))
ontology.properties.append(OntoObject(pk=1400, label="used warp", id="L7"))
ontology.properties.append(OntoObject(pk=1401, label="used weave", id="L8"))
ontology.properties.append(OntoObject(pk=1402, label="used weft", id="L9"))
ontology.properties.append(OntoObject(pk=1403, label="used yarn", id="L10"))
ontology.properties.append(OntoObject(pk=1404, label="has weave type", id="L11"))
ontology.properties.append(OntoObject(pk=1405, label="has motif type", id="L12"))
ontology.properties.append(OntoObject(pk=1406, label="has warping type (deprecated)", id="L13"))
ontology.properties.append(OntoObject(pk=1407, label="used specific weaving technique", id="L14"))
ontology.properties.append(OntoObject(pk=1408, label="has weft type", id="L15"))
ontology.properties.append(OntoObject(pk=1410, label="has quality type", id="P23"))
ontology.properties.append(OntoObject(pk=1411, label="pertains to", id="P13"))
ontology.properties.append(OntoObject(pk=1414, label="is life of", id="P26"))
ontology.properties.append(OntoObject(pk=1435, label="stemmed from", id="P22"))
ontology.properties.append(OntoObject(pk=1436, label="had partner", id="P20"))
ontology.properties.append(OntoObject(pk=1437, label="has type of interaction", id="P21"))
ontology.properties.append(OntoObject(pk=1439, label="has its origins in", id="P24"))
ontology.properties.append(OntoObject(pk=1599, label="took place at", id="P6"))
ontology.properties.append(OntoObject(pk=1851, label="has specific location", id="P48"))
ontology.properties.append(OntoObject(pk=1852, label="has location", id="P49"))
ontology.properties.append(OntoObject(pk=1854, label="has legal location type", id="P51"))
ontology.properties.append(OntoObject(pk=1881, label="is location in or on", id="P52"))
ontology.properties.append(OntoObject(pk=1085, label="encountered object", id="O19"))
ontology.properties.append(OntoObject(pk=1658, label="has use type", id="P29"))
ontology.properties.append(OntoObject(pk=1661, label="is use of", id="P32"))
ontology.properties.append(OntoObject(pk=1860, label="is physical man-made thing type of", id="P1"))
ontology.properties.append(OntoObject(pk=1431, label="the investigation concerns", id="P1"))
ontology.properties.append(OntoObject(pk=1432, label="is requested as a witness", id="P2"))
ontology.properties.append(OntoObject(pk=1433, label="is documented in", id="P3"))
ontology.properties.append(OntoObject(pk=1516, label="has motivation", id="P4"))
ontology.properties.append(OntoObject(pk=1517, label="has motivation type", id="P5"))
ontology.properties.append(OntoObject(pk=1613, label="has duration", id="P6"))
ontology.properties.append(OntoObject(pk=1616, label="mentions geographical place", id="P7"))
ontology.properties.append(OntoObject(pk=1617, label="concerns", id="P8"))
ontology.properties.append(OntoObject(pk=1618, label="has time lapse before account", id="P9"))
ontology.properties.append(OntoObject(pk=1619, label="refers to", id="P10"))
ontology.properties.append(OntoObject(pk=1620, label="has frequency classification", id="P11"))
ontology.properties.append(OntoObject(pk=1621, label="has as a minimum duration", id="P12"))
ontology.properties.append(OntoObject(pk=1622, label="has as a maximum duration", id="P13"))
ontology.properties.append(OntoObject(pk=1623, label="has time lapse of last journey before account", id="P14"))
ontology.properties.append(OntoObject(pk=1627, label="has marital status", id="P15"))
ontology.properties.append(OntoObject(pk=1892, label="has intermediary", id="P16"))
ontology.properties.append(OntoObject(pk=1040, label="effects", id="P3"))
ontology.properties.append(OntoObject(pk=1041, label="ends", id="P4"))
ontology.properties.append(OntoObject(pk=1344, label="is participation of", id="P10"))
ontology.properties.append(OntoObject(pk=1346, label="is participation in the quality of", id="P12"))
ontology.properties.append(OntoObject(pk=1409, label="involves partner", id="P15"))
ontology.properties.append(OntoObject(pk=1434, label="has relationship type", id="P16"))
ontology.properties.append(OntoObject(pk=1445, label="has relationship source", id="P17"))
ontology.properties.append(OntoObject(pk=1446, label="has relationship target", id="P18"))
ontology.properties.append(OntoObject(pk=1784, label="is interaction of", id="P41"))
ontology.properties.append(OntoObject(pk=2270, label="has quality during membership", id="P63"))
ontology.properties.append(OntoObject(pk=2896, label="has role quality", id="P72"))
ontology.properties.append(OntoObject(pk=2897, label="is social relationship role of", id="P73"))
ontology.properties.append(OntoObject(pk=2898, label="is role within", id="P74"))
ontology.properties.append(OntoObject(pk=120, label="spatiotemporally overlaps with", id="P132"))
ontology.properties.append(OntoObject(pk=1412, label="has social quality", id="P14"))
ontology.properties.append(OntoObject(pk=1443, label="takes place at", id="P6"))
ontology.properties.append(OntoObject(pk=1444, label="on behalf of", id="P7"))
ontology.properties.append(OntoObject(pk=1863, label="belongs to activity domain", id="P55"))
ontology.properties.append(OntoObject(pk=1598, label="has type", id="P1"))
ontology.properties.append(OntoObject(pk=1636, label="has measurement unit", id="P12"))
ontology.properties.append(OntoObject(pk=1637, label="has measurement unit", id="P13"))
ontology.properties.append(OntoObject(pk=1638, label="has measurement unit", id="P14"))
ontology.properties.append(OntoObject(pk=1639, label="has measurement unit", id="P15"))
ontology.properties.append(OntoObject(pk=1653, label="effects", id="P8"))
ontology.properties.append(OntoObject(pk=1654, label="ends", id="P9"))
ontology.properties.append(OntoObject(pk=1655, label="belongs to", id="P27"))
ontology.properties.append(OntoObject(pk=1656, label="has part", id="P28"))
ontology.properties.append(OntoObject(pk=1657, label="is composed of part of type", id="P17"))
ontology.properties.append(OntoObject(pk=1659, label="is use by", id="P30"))
ontology.properties.append(OntoObject(pk=1660, label="has purpose", id="P31"))
ontology.properties.append(OntoObject(pk=993, label="created a realisation of", id="R19"))
ontology.properties.append(OntoObject(pk=1015, label="has representative manifestation product type", id="R41"))
ontology.properties.append(OntoObject(pk=1595, label="used specific expression", id="P1"))
ontology.properties.append(OntoObject(pk=1596, label="created manifestation", id="P2"))
ontology.properties.append(OntoObject(pk=1597, label="published the work of", id="P3"))
ontology.properties.append(OntoObject(pk=1644, label="requires the use of", id="P6"))
ontology.properties.append(OntoObject(pk=1645, label="has material", id="P7"))
ontology.properties.append(OntoObject(pk=1646, label="has volume", id="P8"))
ontology.properties.append(OntoObject(pk=1647, label="has planned duration", id="P9"))
ontology.properties.append(OntoObject(pk=1648, label="has weight", id="P10"))
ontology.properties.append(OntoObject(pk=1649, label="shall be performed after", id="P11"))
ontology.properties.append(OntoObject(pk=1650, label="has step type", id="P12"))
ontology.properties.append(OntoObject(pk=1651, label="has procedure type", id="P13"))
ontology.properties.append(OntoObject(pk=1652, label="foresees the use of specific object", id="P14"))
ontology.properties.append(OntoObject(pk=1748, label="is connotation of", id="P39"))
ontology.properties.append(OntoObject(pk=2921, label="classifies with", id="P34"))
ontology.properties.append(OntoObject(pk=2923, label="is realised in", id="P35"))
ontology.properties.append(OntoObject(pk=1609, label="is defined in relation to", id="P19"))
ontology.properties.append(OntoObject(pk=1610, label="is subjection of", id="P8"))
ontology.properties.append(OntoObject(pk=1611, label="is right of", id="P9"))
ontology.properties.append(OntoObject(pk=1626, label="is embodiment by", id="P26"))
ontology.properties.append(OntoObject(pk=1630, label="has holding of a right type", id="P29"))
ontology.properties.append(OntoObject(pk=1632, label="realizes", id="P31"))
ontology.properties.append(OntoObject(pk=1634, label="is embodiment of", id="P33"))
ontology.properties.append(OntoObject(pk=1643, label="is defined by", id="P35"))
ontology.properties.append(OntoObject(pk=1739, label="pertains to", id="P36"))
ontology.properties.append(OntoObject(pk=1777, label="involves legal quality", id="P37"))
ontology.properties.append(OntoObject(pk=1778, label="has legal connotation type", id="P38"))
ontology.properties.append(OntoObject(pk=1779, label="has type", id="P39"))
ontology.properties.append(OntoObject(pk=1785, label="has maximal projection in geographical space", id="P45"))
ontology.properties.append(OntoObject(pk=1807, label="is acquisition by", id="P43"))
ontology.properties.append(OntoObject(pk=1808, label="is acquisition of", id="P44"))
ontology.properties.append(OntoObject(pk=1809, label="issued by", id="P45"))
ontology.properties.append(OntoObject(pk=1810, label="has legal quality acquisition type", id="P46"))
ontology.properties.append(OntoObject(pk=1853, label="has social role type", id="P50"))
ontology.properties.append(OntoObject(pk=1857, label="is legal connotation of", id="P52"))
ontology.properties.append(OntoObject(pk=1944, label="is in relation to", id="P62"))
ontology.properties.append(OntoObject(pk=2416, label="is defined in the context of", id="P69"))
ontology.properties.append(OntoObject(pk=2436, label="is embodied in", id="P70"))
ontology.properties.append(OntoObject(pk=2437, label="has political or administrative entity type", id="P71"))
ontology.properties.append(OntoObject(pk=1631, label="is validity of", id="P30"))
ontology.properties.append(OntoObject(pk=1633, label="has custom or law type", id="P32"))
ontology.properties.append(OntoObject(pk=1780, label="is valid in", id="P40"))
ontology.properties.append(OntoObject(pk=1500, label="belongs to", id="P14"))
ontology.properties.append(OntoObject(pk=1781, label="is valid identifier of", id="P18"))
ontology.properties.append(OntoObject(pk=1782, label="is identification of", id="P18"))
ontology.properties.append(OntoObject(pk=1095, label="removed part or all of", id="AP5"))
ontology.properties.append(OntoObject(pk=1107, label="is embedding of", id="AP18"))
ontology.properties.append(OntoObject(pk=1108, label="is embedding in", id="AP19"))
ontology.properties.append(OntoObject(pk=1799, label="has archeological excavation type", id="P1"))
ontology.properties.append(OntoObject(pk=1801, label="has excavation process unit type", id="P2"))
ontology.properties.append(OntoObject(pk=1802, label="overlies", id="P3"))
ontology.properties.append(OntoObject(pk=1803, label="cuts", id="P4"))
ontology.properties.append(OntoObject(pk=1600, label="is section of", id="BP1"))
ontology.properties.append(OntoObject(pk=1742, label="has quality dimension", id="P35"))
ontology.properties.append(OntoObject(pk=1894, label="has dimension type", id="P25"))
ontology.properties.append(OntoObject(pk=1826, label="concerns", id="P6"))
ontology.properties.append(OntoObject(pk=1827, label="is carried out by", id="P7"))
ontology.properties.append(OntoObject(pk=1828, label="carried out at", id="P8"))
ontology.properties.append(OntoObject(pk=1829, label="has rank", id="P9"))
ontology.properties.append(OntoObject(pk=1830, label="has as disciplinary area", id="P10"))
ontology.properties.append(OntoObject(pk=1805, label="is study at", id="P1"))
ontology.properties.append(OntoObject(pk=1806, label="is the study by", id="P2"))
ontology.properties.append(OntoObject(pk=1811, label="was obtained by", id="P3"))
ontology.properties.append(OntoObject(pk=1812, label="is obtention of", id="P4"))
ontology.properties.append(OntoObject(pk=1815, label="has academic supervisor", id="P5"))
ontology.properties.append(OntoObject(pk=1831, label="is delivered by", id="P11"))
ontology.properties.append(OntoObject(pk=1832, label="is study of", id="P12"))
ontology.properties.append(OntoObject(pk=1833, label="is obtained at", id="P13"))
ontology.properties.append(OntoObject(pk=2932, label="classifies with", id="P87"))
ontology.properties.append(OntoObject(pk=2933, label="classifies", id="P88"))
ontology.properties.append(OntoObject(pk=1847, label="take care of", id="P1"))
ontology.properties.append(OntoObject(pk=1848, label="has caretaker", id="P2"))
ontology.properties.append(OntoObject(pk=1849, label="concerned person", id="P3"))
ontology.properties.append(OntoObject(pk=1850, label="concerned school", id="P4"))
ontology.properties.append(OntoObject(pk=1855, label="has taking care type", id="P5"))
ontology.properties.append(OntoObject(pk=1856, label="has attending a school type", id="P6"))
ontology.properties.append(OntoObject(pk=1642, label="is participation on behalf of", id="P34"))
ontology.properties.append(OntoObject(pk=1893, label="is quality in relation to", id="P57"))
ontology.properties.append(OntoObject(pk=1216, label="is reproduction of", id="P1"))
ontology.properties.append(OntoObject(pk=1334, label="refers to", id="P9"))
ontology.properties.append(OntoObject(pk=1762, label="has definition", id="P18"))
ontology.properties.append(OntoObject(pk=1763, label="has comment", id="P19"))
ontology.properties.append(OntoObject(pk=1864, label="has value version", id="P20"))
ontology.properties.append(OntoObject(pk=1865, label="has text type", id="P21"))
ontology.properties.append(OntoObject(pk=1866, label="has comment type", id="P22"))
ontology.properties.append(OntoObject(pk=1872, label="is annotated in", id="P23"))
ontology.properties.append(OntoObject(pk=1874, label="at position", id="P24"))
ontology.properties.append(OntoObject(pk=1875, label="annotated entity", id="P25"))
ontology.properties.append(OntoObject(pk=1876, label="mentions", id="P26"))
ontology.properties.append(OntoObject(pk=1877, label="is mentioned in", id="P27"))
ontology.properties.append(OntoObject(pk=1878, label="at position", id="P28"))
ontology.properties.append(OntoObject(pk=1879, label="has value", id="P29"))
ontology.properties.append(OntoObject(pk=1889, label="is about", id="P30"))
ontology.properties.append(OntoObject(pk=2214, label="has datation value", id="P26"))
ontology.properties.append(OntoObject(pk=2272, label="has datation type", id="P27"))
ontology.properties.append(OntoObject(pk=2415, label="has mentioning content", id="P31"))
ontology.properties.append(OntoObject(pk=140, label="has parent", id="P152"))
ontology.properties.append(OntoObject(pk=1871, label="comprend", id="P8"))
ontology.properties.append(OntoObject(pk=1895, label="has information object type", id="P26"))
ontology.properties.append(OntoObject(pk=1922, label="effects dedication", id="P21"))
ontology.properties.append(OntoObject(pk=1923, label="has dedicatory object", id="P22"))
ontology.properties.append(OntoObject(pk=1924, label="has dedicatee", id="P23"))
ontology.properties.append(OntoObject(pk=1925, label="has conceptual dedicatee", id="P24"))
ontology.properties.append(OntoObject(pk=1926, label="has beneficiary", id="P25"))
ontology.properties.append(OntoObject(pk=1039, label="included performed version of", id="R66"))
ontology.properties.append(OntoObject(pk=1927, label="is about", id="P58"))
ontology.properties.append(OntoObject(pk=1928, label="is quality of", id="P59"))
ontology.properties.append(OntoObject(pk=1930, label="is quality on behalf of", id="P61"))
ontology.properties.append(OntoObject(pk=1931, label="has performance type", id="P27"))
ontology.properties.append(OntoObject(pk=1797, label="has activity type", id="P19"))
ontology.properties.append(OntoObject(pk=2109, label="moved from", id="P60"))
ontology.properties.append(OntoObject(pk=2110, label="moved to", id="P61"))
ontology.properties.append(OntoObject(pk=2111, label="displaces", id="P62"))
ontology.properties.append(OntoObject(pk=2112, label="has move identifying type", id="P29"))
ontology.properties.append(OntoObject(pk=2116, label="is movement of", id="P1"))
ontology.properties.append(OntoObject(pk=2117, label="has movement identifying type", id="P2"))
ontology.properties.append(OntoObject(pk=2118, label="has stopover identifying type", id="P3"))
ontology.properties.append(OntoObject(pk=2119, label="is journey of", id="P4"))
ontology.properties.append(OntoObject(pk=2120, label="has carrier's journey identifying type", id="P5"))
ontology.properties.append(OntoObject(pk=2121, label="is coerced displacement of", id="P6"))
ontology.properties.append(OntoObject(pk=2122, label="has actor's coerced trip identifying type", id="P7"))
ontology.properties.append(OntoObject(pk=2123, label="is continuation of", id="P8"))
ontology.properties.append(OntoObject(pk=1075, label="observed property type", id="O9"))
ontology.properties.append(OntoObject(pk=2128, label="observed entity type", id="P30"))
ontology.properties.append(OntoObject(pk=1183, label="at distance", id="P16"))
ontology.properties.append(OntoObject(pk=1945, label="is inside or relative to", id="P57"))
ontology.properties.append(OntoObject(pk=1946, label="has relative location type", id="P58"))
ontology.properties.append(OntoObject(pk=1947, label="is quality of", id="P59"))
ontology.properties.append(OntoObject(pk=2257, label="was or is composed of object of type", id="P66"))
ontology.properties.append(OntoObject(pk=1641, label="is intention of", id="P7"))
ontology.properties.append(OntoObject(pk=2299, label="classifies", id="P72"))
ontology.properties.append(OntoObject(pk=2300, label="classifies with", id="P73"))
ontology.properties.append(OntoObject(pk=2274, label="has type of participation", id="P64"))
ontology.properties.append(OntoObject(pk=2312, label="planned move from", id="P28"))
ontology.properties.append(OntoObject(pk=2313, label="planned move to", id="P29"))
ontology.properties.append(OntoObject(pk=2314, label="has component dimension", id="P30"))
ontology.properties.append(OntoObject(pk=2315, label="has quantifiable component type", id="P31"))
ontology.properties.append(OntoObject(pk=2310, label="has epistemic situation preferred type", id="P74"))
ontology.properties.append(OntoObject(pk=2316, label="is quantifiable quality of", id="P76"))
ontology.properties.append(OntoObject(pk=2317, label="is involvement in", id="P77"))
ontology.properties.append(OntoObject(pk=2318, label="has involvement type", id="P78"))
ontology.properties.append(OntoObject(pk=2319, label="is involvement of", id="P79"))
ontology.properties.append(OntoObject(pk=2311, label="is quantifiable quality of", id="P75"))
ontology.properties.append(OntoObject(pk=2320, label="is linked to", id="P80"))
ontology.properties.append(OntoObject(pk=2321, label="has link type", id="P81"))
ontology.properties.append(OntoObject(pk=2324, label="classifies", id="P82"))
ontology.properties.append(OntoObject(pk=2325, label="classifies with", id="P83"))
ontology.properties.append(OntoObject(pk=2368, label="has participation relation type", id="P65"))
ontology.properties.append(OntoObject(pk=2369, label="is participation relation of", id="P66"))
ontology.properties.append(OntoObject(pk=2370, label="is role in", id="P67"))
ontology.properties.append(OntoObject(pk=2371, label="has role quality", id="P68"))
ontology.properties.append(OntoObject(pk=1741, label="has content", id="P34"))
ontology.properties.append(OntoObject(pk=1800, label="has intentional expression identifying type", id="P48"))
ontology.properties.append(OntoObject(pk=1929, label="is quality in relation to intentional event", id="P60"))
ontology.properties.append(OntoObject(pk=2941, label="is quantifiable quality of", id="P89"))
ontology.properties.append(OntoObject(pk=2951, label="has Quantifiable Quality of an Intentional Event type", id="P90"))
ontology.properties.append(OntoObject(pk=45, label="has former or current keeper", id="P49"))
ontology.properties.append(OntoObject(pk=46, label="has current keeper", id="P50"))
ontology.properties.append(OntoObject(pk=47, label="has former or current owner", id="P51"))
ontology.properties.append(OntoObject(pk=62, label="lists", id="P71"))
ontology.properties.append(OntoObject(pk=80, label="brought into existence", id="P92"))
ontology.properties.append(OntoObject(pk=141, label="occupies", id="P156"))
ontology.properties.append(OntoObject(pk=142, label="is at rest relative to", id="P157"))
ontology.properties.append(OntoObject(pk=1067, label="diminished", id="O1"))
ontology.properties.append(OntoObject(pk=1078, label="has dimension", id="O12"))
ontology.properties.append(OntoObject(pk=1081, label="occupied", id="O15"))
ontology.properties.append(OntoObject(pk=1918, label="was a presence of", id="P195"))
ontology.properties.append(OntoObject(pk=1919, label="defines", id="P196"))
ontology.properties.append(OntoObject(pk=1921, label="holds or supports", id="P198"))
ontology.properties.append(OntoObject(pk=2113, label="contains", id="O25"))
ontology.properties.append(OntoObject(pk=2327, label="affects", id="pc1"))
ontology.properties.append(OntoObject(pk=2328, label="has connection through", id="pc3"))
ontology.properties.append(OntoObject(pk=2329, label="shows building feature", id="pc4"))
ontology.properties.append(OntoObject(pk=2332, label="is connected through", id="pc7"))
ontology.properties.append(OntoObject(pk=2333, label="is connected to", id="pc8"))
ontology.properties.append(OntoObject(pk=2335, label="belongs to", id="pc10"))
ontology.properties.append(OntoObject(pk=2338, label="is regulated by", id="pc13"))
ontology.properties.append(OntoObject(pk=2340, label="shows plan configuration type", id="pc15"))
ontology.properties.append(OntoObject(pk=2341, label="shows structural system", id="pc16"))
ontology.properties.append(OntoObject(pk=2342, label="has performance efficiency documented in", id="pc17"))
ontology.properties.append(OntoObject(pk=2343, label="has physical relation with", id="pc18"))
ontology.properties.append(OntoObject(pk=2347, label="shows building homogeneity with", id="pc20"))
ontology.properties.append(OntoObject(pk=2348, label="addressed", id="pc21"))
ontology.properties.append(OntoObject(pk=2349, label="has type", id="pc21_1"))
ontology.properties.append(OntoObject(pk=2352, label="occurred in", id="pc24"))
ontology.properties.append(OntoObject(pk=2353, label="occurs in", id="pc25"))
ontology.properties.append(OntoObject(pk=2354, label="is illustrated by", id="pc26"))
ontology.properties.append(OntoObject(pk=2358, label="resulted in", id="pc30"))
ontology.properties.append(OntoObject(pk=2359, label="transformed", id="pc31"))
ontology.properties.append(OntoObject(pk=2380, label="was embodied by", id="pc42"))
ontology.properties.append(OntoObject(pk=2873, label="shows as construction component", id="pc67"))
ontology.properties.append(OntoObject(pk=2922, label="is of biological object classification type", id="P86"))
ontology.properties.append(OntoObject(pk=2934, label="has propositional object type", id="P32"))
ontology.properties.append(OntoObject(pk=1858, label="is in relation to", id="P53"))
ontology.properties.append(OntoObject(pk=1888, label="carried out in the context of", id="P56"))
ontology.properties.append(OntoObject(pk=2998, label="is presence of", id="P75"))
ontology.properties.append(OntoObject(pk=2999, label="is presence in", id="P76"))
ontology.properties.append(OntoObject(pk=3000, label="has type of presence", id="P77"))
ontology.properties.append(OntoObject(pk=3001, label="has economic transaction identifying type", id="P78"))

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
   J2_concludedThat = 1248
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
   P25_hasDimensionType = 1894
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
   P60_isQualityInRelationToIntentionalEvent = 1929
   P89_isQuantifiableQualityOf = 2941
   P90_hasQuantifiableQualityOfAnIntentionalEventType = 2951
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
   P53_isInRelationTo = 1858
   P56_carriedOutInTheContextOf = 1888
   P75_isPresenceOf = 2998
   P76_isPresenceIn = 2999
   P77_hasTypeOfPresence = 3000
   P78_hasEconomicTransactionIdentifyingType = 3001

properties = PkProperty()

