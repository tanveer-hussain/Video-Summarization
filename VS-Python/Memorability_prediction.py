class Memorability_Prediction:
    
    def mem_calculation(frame1):
        #print ("Inside mem_calculation function")
        start_time1 = time.time()
        resized_image = caffe.io.resize_image(frame1,[227,227])
        net1.blobs['data'].data[...] = transformer1.preprocess('data', resized_image)
        
        
        value = net1.forward()
        value = value['fc8-euclidean']
        end_time1 = time.time()
        execution_time1 = end_time1 - start_time1
        #print ("*********** \t Execution Time in Memobarility = ", execution_time1, " secs \t***********")
        return value[0][0]