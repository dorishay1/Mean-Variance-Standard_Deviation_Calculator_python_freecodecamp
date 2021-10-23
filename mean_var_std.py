import numpy as np

def calculate(num_list):
    
    #error
    if len(num_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #main function
    elif len(num_list) == 9:
        #flat
        mean_f = np.mean(num_list)
        var_f = np.var(num_list)
        std_f = np.std(num_list)
        max_f = np.max(num_list)
        min_f = np.min(num_list)
        sum_f = np.sum(num_list)
        
        num_list = np.array(num_list)
        num_mat = num_list.reshape(3,3)
        
        #axis1
        mean_ax1 = list(np.mean(num_mat, axis=0))
        var_ax1 = list(np.var(num_mat, axis=0))
        std_ax1 = list(np.std(num_mat, axis=0))
        max_ax1 = list(np.max(num_mat, axis=0))
        min_ax1 = list(np.min(num_mat, axis=0))
        sum_ax1 = list(np.sum(num_mat, axis=0))
        
        #axis2
        mean_ax2 = list(np.mean(num_mat, axis=1))
        var_ax2 = list(np.var(num_mat, axis=1))
        std_ax2 = list(np.std(num_mat, axis=1))
        max_ax2 = list(np.max(num_mat, axis=1))
        min_ax2 = list(np.min(num_mat, axis=1))
        sum_ax2 = list(np.sum(num_mat, axis=1))
        
        
        #final dic
        calculations = {
            'mean': [mean_ax1, mean_ax2, mean_f],
            'variance': [var_ax1, var_ax2, var_f],
            'standard deviation': [std_ax1, std_ax2, std_f],
            'max': [max_ax1, max_ax2, max_f],
            'min': [min_ax1, min_ax2, min_f],
            'sum': [sum_ax1, sum_ax2, sum_f]
}
        
        return calculations









#def calculate(list):




 #   return calculations