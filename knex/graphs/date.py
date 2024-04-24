from typing import Tuple
import pandas as pd
from spacy.tokens import Span
from ..constants.ontology import *
from ..globals import graph, params

def link_date(pk_event: int, date_span: Span) -> None:

    # If the date is something like "in 1987" or "in 10.10.2023"
    if 'in' in date_span.text or 'on' in date_span.text:
        date_tuple = __parse_date(date_span.text.replace('in', '').replace('on', ''))
        pk_date = graph.create_entity(class_E61_timePrimitive, span=date_span, text=str(date_tuple), is_orphan=False)
        graph.add_triple(pk_event, property_P82_atSomeTimeWithin, pk_date)

        if params.debug or 'date' in params.debug_list:
            print(f'> Date "at some time within" {date_span.text}')

    # All other cases are "in some time within"
    else:
        date_tuple = __parse_date(date_span.text)
        pk_date = graph.create_entity(class_E61_timePrimitive, span=date_span, text=str(date_tuple), is_orphan=False)
        graph.add_triple(pk_event, property_P82_atSomeTimeWithin, pk_date)

        if params.debug or 'date' in params.debug_list:
            print(f'> Date "At some time within" {date_span.text}')





# Correctly parse a date
def __parse_date(date: str) -> Tuple[int, int, int]:
    if isinstance(date, Span): date_str = date.text
    else: date_str = date

    date_str = date_str.replace('of ', '').replace(',', '').replace('the', '')

    # If the date has a space, it is most probably a string date
    if ' ' in date_str:
        date_elements = date_str.split(' ')
        day = pd.NA
        month = pd.NA
        for elmt in date_elements:
            if 'january' in elmt.lower(): month = 1
            elif 'february' in elmt.lower(): month = 2
            elif 'march' in elmt.lower(): month = 3
            elif 'april' in elmt.lower(): month = 4
            elif 'may' in elmt.lower(): month = 5
            elif 'june' in elmt.lower(): month = 6
            elif 'july' in elmt.lower(): month = 7
            elif 'august' in elmt.lower(): month = 8
            elif 'september' in elmt.lower(): month = 9
            elif 'october' in elmt.lower(): month = 10
            elif 'november' in elmt.lower(): month = 11
            elif 'december' in elmt.lower(): month = 12
            elif 'st' in elmt or 'nd' in elmt or 'rd' in elmt or 'th' in elmt:
                day = int(elmt.replace('st', '').replace('nd', '').replace('rd', '').replace('th', ''))
            else: 
                year = int(elmt)
        return str((year, month, day))
    
    # Else we assume that it is in the wanted format
    else:
        splitted = date_str.split('.')
        if len(splitted) == 3: return str((int(splitted[2]), int(splitted[1]), int(splitted[0].replace('th', ''))))
        return str((int(date_str), pd.NA, pd.NA))