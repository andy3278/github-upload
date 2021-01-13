import numpy as np
import matplotlib.pyplot as plt
def generate_examples(num=1000):
    w = [1.0,-3.0]
    b = 1.0
    
    W = np.reshape(w,(2,1))
    
    X = np.random.randn(num,2)
    
    y = b + np.dot(X, W)
    
    y = np.reshape(y,(num,1))
    
    return X,y
X, y = generate_examples()
#print(X.shape,y.shape)
#print(X[0],y[0])

class Model :
    def __init__ (self, num_features) :
        self.num_features = num_features
        self.W = np.random.randn(num_features , 1)
        self.b = np.random.randn()
    def forward_pass(self,X):
        y_hat = self.b + np.dot(X, self.W)
        return y_hat
    def compute_loss(self,y_hat, y_true):
        return np.sum(np.square(y_hat - y_true))/(2*y_hat.shape[0])
    def backward_pass(self, X, y_true, y_hat):
        m = y_hat.shape[0]
        db = (1/m)*np.sum(y_hat - y_true) 
        dW = (1/m)*np.sum(np.dot(np.transpose(y_hat - y_true), X), axis = 0)
        return dW, db
    def update_params(self, dW, db, lr) : #lr = learning rate
        self.W = self.W - lr*np.reshape(dW, (self.num_features, 1))
        self.b = self.b - db
    def train(self, x_train, y_train, iterations, lr):
        losses = []
        for i in range(0, iterations):
            y_hat = self.forward_pass(x_train)
            loss = self.compute_loss(y_hat, y_train)
            dW, db = self.backward_pass(x_train, y_train, y_hat)
            self.update_params(dW, db, lr)
            losses.append(loss)
            if i%int(iterations/10) == 0 :
                print("Iter: {}, Loss: {:.4f}" .format(i, loss))
        return losses
y_hat = Model(2).forward_pass(X)
print(y_hat.shape)
model = Model(2)
y_hat = model.forward_pass(X)
#bakcward pass
dW, db = model.backward_pass(X, y, y_hat)
x_train, y_train = generate_examples()
losses = model.train(x_train, y_train, 1000, 3e-3)
#plt.plot(losses)
loss = model.compute_loss(y_hat, y)
print(dW, db)
model_untrained = Model(2)
x_test, y_test = generate_examples(500)
print(x_test.shape, y_test.shape)
preds_untrained = model_untrained.forward_pass(x_test)
preds_trained = model.forward_pass(x_test)
plt.figure(figsize = (6, 6))
plt.plot(preds_untrained, y_test, "rx", label = "Untrained")
plt.plot(preds_trained, y_test, "b.", label = "Trianed")
plt.legend()
plt.xlabel("Predictions")
plt.ylabel("Ground Truth")
plt.show()