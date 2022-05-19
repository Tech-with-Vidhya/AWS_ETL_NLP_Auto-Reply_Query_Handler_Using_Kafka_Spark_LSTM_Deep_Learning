
import numpy as np

from .References import References

class EvaluateModel(References):


    def evaluate_model(self, X_test, Y_test, model):
        """Evaluate the model"""
        validation_size = 1500

        X_validate = X_test[-validation_size:]
        Y_validate = Y_test[-validation_size:]

        score, acc = model.evaluate(X_test, Y_test, verbose=2, batch_size=self.BATCH_SIZE_BINARY_EVALUATE)
        print("score: %.2f" % (score))
        print("acc: %.2f" % (acc))
        return X_validate, Y_validate


    def class_based_accuracy(self, X_validate, Y_validate, X_test, model):
        """Evaluate the model by getting class based accuracy"""

        pos_cnt, neg_cnt, pos_correct, neg_correct = self.ZERO, self.ZERO, self.ZERO, self.ZERO
        for x in range(len(X_validate)):
            result = model.predict(X_validate[x].reshape(1, X_test.shape[1]), batch_size=self.ONE, verbose=self.ZERO)[0]

            if np.argmax(result) == np.argmax(Y_validate[x]):
                if np.argmax(Y_validate[x]) == self.ZERO:
                    neg_correct += self.ONE
                else:
                    pos_correct += self.ONE

            if np.argmax(Y_validate[x]) == self.ZERO:
                neg_cnt += self.ONE
            else:
                pos_cnt += self.ONE

        print("pos_acc", pos_correct / pos_cnt * 100, "%")
        print("neg_acc", neg_correct / neg_cnt * 100, "%")
