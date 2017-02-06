function dataana
Data = load('test.data');

disp(Data(:, 2));

mean(Data(:, 2), 1)
endfunction