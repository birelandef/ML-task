%% Multiply Two Vectors  

%% 
% Create a 1-by-4 row vector, |A|, and a 4-by-1 column vector, |B|. 
A = [1 1 0 0];
B = [1; 2; 3; 4];  

%% 
% Multiply |A| times |B|. 
C = A*B 

%%
% The result is a 1-by-1 scalar, also called the _dot product_ or _inner
% product_ of the vectors |A| and |B|. Alternatively, you can calculate
% the dot product $A \cdot B$ with the syntax |dot(A,B)|.  

%% 
% Multiply |B| times |A|. 
C = B*A 

%%
% The result is a 4-by-4 matrix, also called the _outer product_ of the
% vectors |A| and |B|. The outer product of two vectors, $A \otimes
% B$, returns a matrix.   

