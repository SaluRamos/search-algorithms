import random
import os
import time
import decimal
import math

#embaralha uma lista
def shuffle_list(list_to_shuffle):
    shuffled_list = []
    for i in range(len(list_to_shuffle)):
        elem = random.choice(list_to_shuffle)
        elem_index = list_to_shuffle.index(elem)
        list_to_shuffle.pop(elem_index)
        shuffled_list.append(elem)
    return shuffled_list




#cria uma lista com 'n' elementos inteiros aleatorios que vão de 'min' a 'max'
def create_random_range_list(amount_elems, min, max):
    new_list = []
    for i in range(amount_elems):
        new_list.append(random.randint(min, max))
    return new_list




#cria uma lista com 'n' elementos strings aleatorios que vão de 'min' a 'max'
def create_random_string_list(amount_elems, min_lenght, max_lenght):
    new_list = []
    vocabulary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(amount_elems):
        new_string = ""
        for j in range(random.randint(min_lenght, max_lenght)):
            new_string = new_string + random.choice(vocabulary)
        new_list.append(new_string)
    return new_list




#retorna o index do valor alvo 'target' procurado
#a lista deve estar ordenada
#poder de busca de 2^n
#com 30 recursividades pode encontrar um elemento especifico entre mais de 1 bilhão de elementos.
def binary_search(list_to_search, target, start = 0, end = None):
    if (end == None):
        end = len(list_to_search) - 1
    if (start > end):
        return -1
    middle = math.floor((start + end)/2)
    if (target == list_to_search[middle]):
        return middle
    elif (target < list_to_search[middle]):
        return binary_search(list_to_search, target, start, middle -1)
    return binary_search(list_to_search, target, middle + 1, end)




#retorna o menor valor de uma lista e seu index
def search_lower_value(list_to_search):
    lower = None
    lower_index = None
    for index, i in enumerate(list_to_search):
        if lower == None or i < lower:
            lower = i
            lower_index = index
    return lower_index, lower




#retorna o maior valor de uma lista e seu index
def search_higher_value(list_to_search):
    higher = None
    higher_index = None
    for index, i in enumerate(list_to_search):
        if higher == None or i > higher:
            higher = i
            higher_index = index
    return higher_index, higher




#algoritmo de ordenação 1
def selection_sort(list_to_sort, reverse = False):
    for index_i, current_value in enumerate(list_to_sort):
        lower_index, lower_value = search_lower_value(list_to_sort[index_i:])
        list_to_sort[index_i] = lower_value
        list_to_sort[lower_index + index_i] = current_value
    if reverse == True:
        list_to_sort.reverse()
    return list_to_sort




#algoritmo de ordenação 2
def insertion_sort(list_to_sort, reverse = False):
    for index_i, i in enumerate(list_to_sort):
        for j in range(index_i, 0, -1):
            if list_to_sort[j - 1] > list_to_sort[j]:
                left_elem = list_to_sort[j - 1]
                list_to_sort[j - 1] = list_to_sort[j]
                list_to_sort[j] = left_elem
            else:
                break
    if reverse == True:
        list_to_sort.reverse()
    return list_to_sort




#algoritmo de ordenação 3
def share_sort(list_to_sort, secondary_sort = insertion_sort, reverse = False, amount_sorters = 0):
    #divide o trabalho
    if amount_sorters == 0:
        amount_sorters = math.floor(math.sqrt(len(list_to_sort)))
    sorters = []
    added_elems = 0
    for i in range(math.floor(len(list_to_sort)/amount_sorters)):
        sorters.append(list_to_sort[added_elems:added_elems + amount_sorters])
        added_elems += amount_sorters
    if (len(list_to_sort) - added_elems) > 0:
        sorters.append(list_to_sort[added_elems:])
    #ordena 1
    for index_i, i in enumerate(sorters):
        sorters[index_i] = secondary_sort(sorters[index_i])
    #ordena 2
    new_list = []
    for i in range(len(list_to_sort)):
        lower_list_index = 0
        lower_value = None
        for index_j, j in enumerate(sorters):
            if (lower_value == None) or (j[0] < lower_value):
                lower_value = j[0]
                lower_list_index = index_j
        new_list.append(lower_value)
        sorters[lower_list_index].pop(0)
        if sorters[lower_list_index] == []:
            sorters.pop(lower_list_index)
    if reverse == True:
        new_list.reverse()
    return new_list




#algoritmo de ordenação 4
def merge_sort(list_to_sort, reverse = False, start = 0, end = None):
    if end == None:
        end = len(list_to_sort)
    if (end - start > 1):
        middle = (end + start)//2
        merge_sort(list_to_sort = list_to_sort, start = start, end = middle)
        merge_sort(list_to_sort = list_to_sort, start = middle, end = end)
        merge(list_to_sort, start, middle, end)
    if reverse == True:
        list_to_sort.reverse()
    return list_to_sort

def merge(list_to_sort, start, middle, end):
    left = list_to_sort[start:middle]
    right = list_to_sort[middle:end]
    top_left, top_right = 0, 0
    for i in range(start, end):
        if top_left >= len(left):
            list_to_sort[i] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            list_to_sort[i] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            list_to_sort[i] = left[top_left]
            top_left += 1
        else:
            list_to_sort[i] = right[top_right]
            top_right += 1




#algoritmo de ordenação 5
def quick_sort(list_to_sort, reverse = False, start = 0, end = None):
    if end == None:
        end = len(list_to_sort) - 1
    if start < end:
        p = partition(list_to_sort, start, end)
        quick_sort(list_to_sort = list_to_sort, start = start, end = (p - 1))
        quick_sort(list_to_sort = list_to_sort, start = (p + 1), end = end)
    if reverse == True:
        list_to_sort.reverse()
    return list_to_sort

def partition(list_to_sort, start, end):
    pivot = list_to_sort[end]
    i = start
    for j in range(start, end):
        if list_to_sort[j] <= pivot:
            list_to_sort[j], list_to_sort[i] = list_to_sort[i], list_to_sort[j]
            i += 1
    list_to_sort[i], list_to_sort[end] = list_to_sort[end], list_to_sort[i]
    return i




#executa a função e cronometra a velocidade de execução
#o argumento 'params' deve possuir todos os argumentos da função 'target_function'
#sempre garanta que o argumento/parâmetro 'params' é do tipo tupla! se possuir só um argumento/parâmetro dentro dessa tupla, será '(arg1,)' (COM VÍRGULA!)
def test_function_speed(target_function, params = (), print_function_result = False, precision = 8, extra_info = ""):
    start_time = time.perf_counter()
    result = target_function(*params)
    end_time = time.perf_counter()
    precision_str = "0."
    for i in range(precision):
        precision_str = precision_str + "0"
    performance = decimal.Decimal(f"{end_time - start_time}").quantize(decimal.Decimal(precision_str))
    if print_function_result == True:
        print(f"função '{target_function.__name__}' executada em '{performance}' segundo(s)! {extra_info}")
    return performance, result




#início do software
if __name__ == "__main__":

    os.system("cls")

    shuffled_int_list = create_random_range_list(1000, 1, 999)
    print(f"lista de int's com ordem aleatória criada é {shuffled_int_list[:3]}...{shuffled_int_list[-3:]}\n")

    algorithms = {}

    shuffled_int_list_copy = shuffled_int_list.copy()
    selection_sort_performance, sort_lower_to_higher = test_function_speed(selection_sort, (shuffled_int_list_copy,))
    algorithms['SELECTION SORT'] = selection_sort_performance

    shuffled_int_list_copy = shuffled_int_list.copy()
    insertion_sort_performance, sort_lower_to_higher = test_function_speed(insertion_sort, (shuffled_int_list_copy,))
    algorithms['INSERTION SORT'] = insertion_sort_performance

    shuffled_int_list_copy = shuffled_int_list.copy()
    share_sort_performance_1, sort_lower_to_higher = test_function_speed(share_sort, (shuffled_int_list_copy, insertion_sort), extra_info = "(usando 'insertion_sort' de algoritmo secundário)")
    algorithms['SHARE SORT 1'] = share_sort_performance_1

    shuffled_int_list_copy = shuffled_int_list.copy()
    share_sort_performance_2, sort_lower_to_higher = test_function_speed(share_sort, (shuffled_int_list_copy, selection_sort), extra_info = "(usando 'selection_sort' de algoritmo secundário)")
    algorithms['SHARE SORT 2'] = share_sort_performance_2

    shuffled_int_list_copy = shuffled_int_list.copy()
    merge_sort_performance, sort_lower_to_higher = test_function_speed(merge_sort, (shuffled_int_list_copy,))
    algorithms['MERGE SORT'] = merge_sort_performance

    shuffled_int_list_copy = shuffled_int_list.copy()
    quick_sort_performance, sort_lower_to_higher = test_function_speed(quick_sort, (shuffled_int_list_copy,))
    algorithms['QUICK SORT'] = quick_sort_performance

    shuffled_int_list_copy = shuffled_int_list.copy()
    tim_sort_performance, sort_lower_to_higher = test_function_speed(sorted, (shuffled_int_list_copy,), extra_info = "(usando 'tim_sort' de algoritmo primário)")
    algorithms['TIM SORT'] = tim_sort_performance

    #EXISTE UM ALGORITMO QUE PROMETE SER SUPERIOR AO 'TIM SORT' E 'QUICK SORT', CHAMADO 'QUAD SORT', CRIADO EM 2020
    #ACREDITO QUE A DIFERENÇA DE DESEMPENHO ENTRE O 'TIM SORT' CHAMADO PELA FUNÇÃO 'SORTED' PADRÃO DO PYTHON SEJA CULPA DAS LISTAS, QUE NÃO POSSUEM UM DESEMPENHO MUITO BOM, 'SORTED' DEVE USAR ESTRUTURAS DE LISTA/ARRAY DIFERENTE E MAIS OTIMIZADA

    print("QUANTO MAIS ALTA A PONTUAÇÃO, MELHOR!\n")
    lower_rank_speed = 0
    total_to_rank = len(algorithms)
    for j in range(len(algorithms)):
        lower_speed = None
        pontuation = 0
        for i in algorithms.values():
            if lower_speed == None:
                lower_speed = i
            elif lower_speed < i:
                lower_speed = i
        for i in algorithms.keys():
            if algorithms[i] == lower_speed:
                algorith_name = i
                del algorithms[i]
                break
        if j == 0:
            pontuation = 1
            lower_rank_speed = lower_speed
        else:
            pontuation = lower_rank_speed/lower_speed
        print(f"{total_to_rank - j} lugar = '{round(pontuation, 2)}' ponto(s) | executado em '{lower_speed}' segundo(s) | {algorith_name}")