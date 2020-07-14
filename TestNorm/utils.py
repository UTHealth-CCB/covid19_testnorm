import re
import functools
from collections import Iterable, Counter

def pre_tokenize(text, trip_non_alnum=False, insert_period=False, windows_style=False):  
    """Preprocessing for query text with tokenization.
    insert preceding and subsequent space for non-alphabetnumeric character and replace multiple space with one space

    Args:
        text: input text
        trip_non_alnum: bool, trip non alpha&number character and replace it with ' ' if True else keep all characters, False by default
        inert_period: bool, inser period(.) before '\n' if True, False by default
        windows_style: bool, text's CRLF as '\r\n if windows-style else '\n', False by default    

    Returns:
        Tokenized text
    """
    period = '.' if insert_period else ''
    CRLF = '\r\n' if windows_style else '\n'    
    text = text.replace(CRLF, '.'+CRLF) if text.find(CRLF)>=0 else text+period
    if trip_non_alnum:
        text = ''.join([c if c.isalnum() else ' ' for c in text]) 
    else:
        text = ''.join([c if c.isalnum() else ' '+c+' ' for c in text]) 
    text = re.sub(' +', ' ', text) 
    CRLF_new = period+' \r \n ' if windows_style else period+' \n '
    text = re.sub(CRLF_new, period+CRLF, text)
    text = text.strip(' ') # if no CRLF included, strip ' ' at both sides
    return text

def contains(source, target, whole_match=True, in_order=True, max_match=False):
    """Judge whether source contains target    

    Args:
        source: string or iterable obj, if iterable, each item should be string
        target: string or iterable obj, if iterable, each item should be string 
        whole_match: bool, whether match in whole word, True by default, word is seprated by space or puncs using pre_tokenize function)
        in_order: bool, valid when whole_match is True, whether match the target in tokens' orginal order, True by default, word is seprated by space or puncs using pre_tokenize function)
        max_match: bool, valid when whole_match is True, whether return items that have max-length if there're containable-relations between them (one item is partial part of another), 
                   i.e., for multiple matched target items (non-str target) which have containable-relations, return items that have the max-length among them if max_match is True, else return all matched items, False by default

    Returns:
        Matched target if target is string else return matched items in list for iterable target
    """    
    trip_non_alnum = True
    if type(source) == str:
        source_pt = pre_tokenize(source.lower(), trip_non_alnum)
        if not target:
            return target
        if type(target) == str:
            # lower target until now since we'd like to return target in original form
            target_pt = pre_tokenize(target.lower(), trip_non_alnum)
            if whole_match:
                if in_order:
                    #if target_pt in source_pt.split(' '): # can't different covid-19 and swab for covid-19 and Ab simultaneously: covid-19 (quest)    swab                
                    pattern = r'^'+target_pt+' |^'+target_pt+'$| '+target_pt+' | '+target_pt+'$'
                    if re.search(pattern, source_pt):
                        return target
                else:
                    source_pt_c = Counter(source_pt.split())
                    target_pt_c = Counter(target_pt.split())
                    source_target_inter = source_pt_c & target_pt_c
                    if source_target_inter == target_pt_c:
                        return target
            else:
                if source_pt.find(target_pt) >= 0:
                    return target
                else:
                    return ''
        else:
            ret = []
            for tar in target:
                tar_pt = pre_tokenize(tar.lower(), trip_non_alnum)                
                if whole_match:
                    if in_order:
                        #if tar_pt in source_pt.split(' '):
                        pattern = r'^'+tar_pt+' |^'+tar_pt+'$| '+tar_pt+' | '+tar_pt+'$'
                        if re.search(pattern, source_pt): 
                            append = True
                            drop_dict = []
                            if max_match:
                                for item in ret:                   
                                    if contains(item, tar, whole_match, in_order):
                                        append = False
                                        break
                                    elif contains(tar, item, whole_match, in_order):
                                        drop_dict.append(item)
                            ret[:] = [v for v in ret if v not in drop_dict]                                                                    
                            if append:
                                ret.append(tar)
                    else:
                        source_pt_c = Counter(source_pt.split())
                        tar_pt_c = Counter(tar_pt.split())
                        source_tar_inter = source_pt_c & tar_pt_c
                        if source_tar_inter == tar_pt_c:
                            append = True
                            drop_dict = []
                            if max_match:
                                for item in ret:                   
                                    if contains(item, tar, whole_match, in_order):
                                        append = False
                                        break
                                    elif contains(tar, item, whole_match, in_order):
                                        drop_dict.append(item)
                            ret[:] = [v for v in ret if v not in drop_dict]                                                                    
                            if append:
                                ret.append(tar)                            
                else:
                    if source_pt.find(tar_pt) >= 0:
                        ret.append(tar)
            return ret
    else:
        source_pt = [pre_tokenize(item.lower(), trip_non_alnum) for item in source]
        if not target:
            return target
        if type(target) == str:
            if whole_match:
                target_pt = pre_tokenize(target.lower(), trip_non_alnum)
                if in_order:
                    if  target_pt in source_pt:
                        return target
                    else:
                        return ''
                else:
                    contained = False
                    for src_pt in source_pt:
                        src_pt_c = Counter(src_pt.split())
                        target_pt_c = Counter(target_pt.split())
                        src_target_inter = src_pt_c & target_pt_c
                        if src_target_inter == target_pt_c:
                            contained = True
                            break
                    if contained:
                        return target
                    else:
                        return ''                                   
            else:
                if any(item.find(pre_tokenize(target.lower(), trip_non_alnum))>=0 for item in source_pt):
                    return target
                else:
                    return ''
        else:
            ret = []
            for tar in target:
                tar_pt = pre_tokenize(tar.lower(), trip_non_alnum)
                if whole_match:
                    if in_order:
                        if tar_pt in source_pt:
                            ret.append(tar)
                    else:
                        for src_pt in source_pt:
                            src_pt_c = Counter(src_pt.split())
                            tar_pt_c = Counter(tar_pt.split())
                            src_tar_inter = src_pt_c & tar_pt_c
                            if src_tar_inter == tar_pt_c:
                                append = True
                                if max_match:
                                    for item in ret:                   
                                        if contains(item, tar, whole_match, in_order):
                                            append = False
                                            break
                                if append:
                                    ret.append(tar)
                else:
                    if any(item.find(pre_tokenize(tar.lower(), trip_non_alnum))>=0 for item in source_pt):
                        ret.append(tar)
            return ret

def has_valid_value(obj):
    """Check whether obj has valid values. For iterable obj, return False if all items are not valid else return True."""
    ret = False
    if isinstance(obj, Iterable):
        if type(obj) == dict:
            for _, value in obj.items():
                if value:
                    ret = True
                    break
        else:
            for elem in obj:
                if elem:
                    ret = True
                    break
    else:
        ret = True if obj else False
    return ret