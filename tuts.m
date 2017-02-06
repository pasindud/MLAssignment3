function tuts



Data = load('spam.data');


features = [1, 2, 3,4,5,6,7,8,9,10, ...
            11,12,13,14,15,16,17,18,19,20,...
            21,22,23,24,25,26,27,28,29,30,...
            31,32,33,34,35,36,37,38,39,40,...
            41,42,43,44,45,46,47,48,49,50,...
            51,52,53,54,55,56,57]';

method = "svm";  % use "ridge" "logistic" or "svm"
lambda = 1.0;  % regularisation weight -- doesn't work for logistic

X = Data(:,features);  % Each row of X is a feature vector 

Y = Data(:,58); % Y contains the class labels

N = length(X); % N is the total number of instances

Y(Y==0) = -1;  % Change values of Y to +1 and -1

Ntrain = ceil(0.8*N);  % use 80% of the instances for training

% randomly choose Ntrain instances for training

p = randperm(N);
Xtrain = X(p(1:Ntrain),:);
Ytrain = Y(p(1:Ntrain),:);

% choose the remaining for testing

Xtest = X(p((Ntrain+1):N),:);
Ytest = Y(p((Ntrain+1):N),:);

fprintf('\nSVM - \n')

	[w0, w] = getWeights("svm", Ytrain, Xtrain, lambda);
	disp(w0)
	accuracy(w0, w, Ytest, Xtest)

fprintf('\nridge - \n')
[w0, w] = getWeights("ridge", Ytrain, Xtrain, lambda);
accuracy(w0, w, Ytest, Xtest)


# try
	fprintf('\nlogistic - \n')
	[w0, w] = getWeights("logistic", Ytrain, Xtrain, lambda);
	accuracy(w0, w, Ytest, Xtest)
# catch
# 	fprintf('\n')
# end_try_catch

endfunction

function accuracy (w0, w, Ytest, Xtest)
	Htest = w0 + Xtest*w;
	Yhat = 2*(Htest > 0)-1;
	accuracy = sum(Yhat == Ytest) / length(Ytest)
	# sensitivity = sum(Yhat(Ytest==1) == 1) / length(Ytest == 1)
endfunction


function [w0, w] = getWeights (method, Ytrain, Xtrain, lambda)
	switch(method)
	  case "logistic"
	    [w0, w] = logistic_regression(Ytrain, Xtrain);
	  case "ridge"
	    [w, w0] = ridge(Xtrain, Ytrain, lambda);
	  case "svm"
	    [w, w0] = lsvmclass(Xtrain, Ytrain, lambda);
	end
endfunction
