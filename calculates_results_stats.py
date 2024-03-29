def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the classroom Item XX Calculating Results for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function
    results_stats_dic = dict()
    results_stats_dic["n_correct_dog"] = 0 # done
    results_stats_dic["n_dogs_img"] = 0 # done
    results_stats_dic["n_correct_notdogs"] = 0 # done
    results_stats_dic["n_correct_breed"] = 0 # done
    results_stats_dic["n_match"] = 0 # done
    for key in results_dic:
        #results_stats_dic.update({results_dic[key][0]:len(results_dic)})
        results_stats_dic['n_images'] = len(results_dic)
        if results_dic[key][3] == 1:             # if true gives number dog image count
            results_stats_dic["n_dogs_img"] +=1
            if results_dic[key][4]==1:  # if index 3 and 4 are true gives "number of  correct dog"
                results_stats_dic["n_correct_dog"] += 1

        if results_dic[key][3] == 0 and results_dic[key][4] == 0:   # if index 4 is false gives "number of correct not dogs"
            results_stats_dic["n_correct_notdogs"] += 1

        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1  # gives the label matches between pet name and classifer name
        if results_dic[key][2] == 1 and results_dic[key][3] == 1:
            results_stats_dic["n_correct_breed"] += 1
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img'] # not dog images
    results_stats_dic["pct_correct_dogs"] = (results_stats_dic["n_correct_dog"] / results_stats_dic['n_dogs_img']) * 100
    results_stats_dic["pct_match"] = (results_stats_dic["n_match"]/results_stats_dic['n_images'])  * 100
    if results_stats_dic["n_notdogs_img"] > 0:
        results_stats_dic["pct_correct_notdogs"] = (results_stats_dic["n_correct_notdogs"] / results_stats_dic["n_notdogs_img"]) * 100
    else:
        results_stats_dic["pct_correct_notdogs"] = 0.0

    results_stats_dic["pct_correct_breed"] = (results_stats_dic["n_correct_breed"] / results_stats_dic["n_dogs_img"]) * 100
    results_stats_dic["pct_correct_label_match"] = (results_stats_dic["n_match"] / len(results_dic)) * 100
    print(results_stats_dic)
    print(results_dic)
    return results_stats_dic
