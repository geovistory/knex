from .globals import index

# Unique index for each Entity
def __get_index():
    global index
    index += 1
    return index
    

# Keep entity in the doc
def get_entity(doc, klass, name):
    same = list(filter(lambda entity: entity['class'] == klass and entity['name'] == name, doc._.entities))

    if len(same) == 1: return same[0]
    else: 
        name_title = name.title()
        to_return = {
            'pk': __get_index(),
            'class': klass,
            'name': name_title,
            'label': f"{name_title} ({klass})"
        }
        doc._.entities.append(to_return)
        return to_return
    

# Expand document graph
def add_triple(doc, triple):
    key = str(triple[0]['pk']) + '-' + str(triple[2]['pk'])
    if key in doc._.graph_keys: return

    doc._.graph_keys.add(key)
    doc._.graph.append({
        'subject_pk': triple[0]['pk'],
        'subject_label': triple[0]['label'],
        'subject_class': triple[0]['class'],
        'property': triple[1],
        'object_pk': triple[2]['pk'],
        'object_label': triple[2]['label'],
        'object_class': triple[2]['class'],
    })

    

