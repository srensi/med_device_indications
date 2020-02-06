# requirements
## sudo apt-get install gawk
## pip3 install merpy

import os
import merpy


def process_list(data_path, list_name):
    """

    :param data_path:
    :param list_name:
    """

    new_list = open(data_path + list_name + '.txt', 'r', encoding='utf-8')
    elements_list = new_list.read().split('\n')
    if len(elements_list) == 1:
        elements_list = ''.join(elements_list)
        elements_list = elements_list.split(',')

    merpy.create_lexicon(elements_list, list_name)
    merpy.process_lexicon(list_name)

    return


def annotations(corpus_path, data_path):
    """

    :param corpus_path:
    :param data_path:
    """

    merpy.download_lexicons()
    merpy.process_lexicon("hp")
    merpy.process_lexicon("doid")
    merpy.process_lexicon("radlex")

    process_list(data_path, 'chebi')
    process_list(data_path, 'medical_devices')
    process_list(data_path, 'temporal_list')
    process_list(data_path, 'population_vocabulary')

    for f in os.listdir(corpus_path):

        file_to_annotate = open(corpus_path + f, 'r', encoding = 'utf-8')
        file_content = file_to_annotate.read()
        file_to_annotate.close()

        entities_hp = merpy.get_entities(file_content, "hp")
        clean_hp_list = []
        for hp in entities_hp:
            if 'HP' not in hp[-1]:
                pass
            else:
                clean_hp_list.append(hp)

        entities_doid = merpy.get_entities(file_content, "doid")
        entities_radlex = merpy.get_entities(file_content, "radlex")
        entities_devices = merpy.get_entities(file_content, "medical_devices")
        entities_chebi = merpy.get_entities(file_content, "chebi")
        entities_temporal = merpy.get_entities(file_content, "temporal")
        entities_population = merpy.get_entities(file_content, "population")

        entities = clean_hp_list + entities_doid + entities_devices + entities_chebi + entities_radlex + entities_temporal + entities_population
        entities_clean = [x for x in entities if x != ['']]

        entities_sorted = sorted(entities_clean, key = lambda position: int(position[0]))

        print('\n' + f + '\n')
        for entity in entities_sorted:
            print(entity)

    return

annotations('corpus/', 'data/')