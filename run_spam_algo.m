
## Author: Neil J. Hurley <neil.hurley.slprog@Neils-MacBook-Air-2.local>
## Created: 2015-01-30

function [accuracy,sensitivity, features] = run_spam_algo (method,lambda,features)

Data = load('spam.data');

%features = [1, 2, 3,4,5,6,7,8,9,10, ...
%            11,12,13,14,15,16,17,18,19,20,...
%            21,22,23,24,25,26,27,28,29,30,...
%            31,32,33,34,35,36,37,38,39,40,...
%            41,42,43,44,45,46,47,48,49,50,...
%            51,52,53,54,55,56,57]';

%method = "svm";  % use "ridge" "logistic" or "svm"
%lambda = 1.0;  % regularisation weight -- doesn't work for logistic

% disp ("The value of features is:"), disp (features)

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


% Now train the model
% Use Logistic classification or Ridge classification or SVM classification

% Note that w0, the bias, is output separately to the other weights

switch(method)
  case "logistic"
    [w0, w] = logistic_regression(Ytrain, Xtrain);
  case "ridge"
    [w, w0] = ridge(Xtrain, Ytrain, lambda);
  case "svm"
    [w, w0] = lsvmclass(Xtrain, Ytrain, lambda);
end


% Apply the model to the test set. The hypothesis is calculated by summing the weights with the test instances

Htest = w0 + Xtest*w;

% Predict that the class is +1 when the hypothesis is positive, otherwise predict that the class is -1

Yhat = 2*(Htest > 0)-1;

%  Some performance results

% fprintf('The accuracy tells us the percentage of test instances that are correctly classified.\n'); 

accuracy = sum(Yhat == Ytest) / length(Ytest)

% fprintf('The sensitivity or recall tells us the percentage of positive instances (i.e. spams emails) that were correctly classified.\n');

sensitivity = sum(Yhat(Ytest==1) == 1) / length(Ytest == 1)

