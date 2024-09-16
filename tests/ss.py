from classifier_anshp import dataset_3,hyper_tunner,model

partial_x,partial_y,x_val,y_val,x_test,y_test = dataset_3()
hyper_tunner(partial_x,partial_y,x_val,y_val,5,0)
module = model()
print(module.predict(x_test))