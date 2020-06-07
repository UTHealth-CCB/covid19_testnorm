import re
import functools
from collections import Iterable

# pre_tokenize: preprocessing for query string
# insert preceding and subsequent space for non-alphabetnumeric character and replace multiple space with one space
# str -- input string
# trip_non_alnum -- trip non alpha&number character and replace it with ' ' if True else keep all characters, False by default
# inert_period -- inser period(.) before '\n' if True, False by default
# windows_style -- str is windows-style for CRLF as '\r\n else '\n', False by default
# return pre-tokenized str
def pre_tokenize(str, trip_non_alnum=False, insert_period=False, windows_style=False):    
    period = '.' if insert_period else ''
    CRLF = '\r\n' if windows_style else '\n'    
    str = str.replace(CRLF, '.'+CRLF) if str.find(CRLF)>=0 else str+period
    if trip_non_alnum:
        str = ''.join([c if c.isalnum() else ' ' for c in str]) 
    else:
        str = ''.join([c if c.isalnum() else ' '+c+' ' for c in str]) 
    str = re.sub(' +', ' ', str) 
    CRLF_new = period+' \r \n ' if windows_style else period+' \n '
    str = re.sub(CRLF_new, period+CRLF, str)
    str = str.strip(' ') # if no CRLF included, strip ' ' at both sides
    return str

# contains(source, target, whole_match=True) 
# judge whether source contains target
# source -- source string or iterable obj, if iterable, each item should be string
# target -- target string or iterable obj, if iterable, each item should be string 
# whole_match -- whether match in whole word, True by default, word is seprated by space or puncs using pre_tokenize function) or partial
# return matched target if target is string else return matched items in list for iterable target
def contains(source, target, whole_match=True):
    trip_non_alnum = True
    if type(source) == str:
        source_pt = pre_tokenize(source.lower(), trip_non_alnum)
        if not target:
            return target
        if type(target) == str:
            # lower target until now since we'd like to return target in original form
            target_pt = pre_tokenize(target.lower(), trip_non_alnum)
            if whole_match:
                #if target_pt in source_pt.split(' '): # can't different covid-19 and swab for covid-19 and Ab simultaneously: covid-19 (quest)    swab                
                pattern = r'^'+target_pt+' |^'+target_pt+'$| '+target_pt+' | '+target_pt+'$'
                if re.search(pattern, source_pt):
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
                    #if tar_pt in source_pt.split(' '):
                    pattern = r'^'+tar_pt+' |^'+tar_pt+'$| '+tar_pt+' | '+tar_pt+'$'
                    if re.search(pattern, source_pt):                    
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
                if pre_tokenize(target.lower(), trip_non_alnum) in source_pt:
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
                if whole_match:
                    if pre_tokenize(tar.lower(), trip_non_alnum) in source_pt:
                        ret.append(tar)                
                else:
                    if any(item.find(pre_tokenize(tar.lower(), trip_non_alnum))>=0 for item in source_pt):
                        ret.append(tar)
            return ret

# check whether obj has valid values. For iterable obj, return False if all items are not valid else return True
def has_valid_value(obj):
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