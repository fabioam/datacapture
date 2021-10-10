# DataCapture

A class used to accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.

The methods add(), less(), greater(), and between() should have
constant time O(1)

## Testing
There are some tests included. To run, execute tests.py:
```
$ python tests.py                                                                                                                                                                                                           1 ↵ 
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s
```


## Time complexity

The sort method use the Radix Sort algorithm and should run at most linear O(n):


<img src="https://gcdn.pbrd.co/images/2LXXj8sYdJQ5.png?o=1">


To run the time complexity tests for the  build_stats() method, execute the steps bellow:

```
$ mkvirtualenv datacapture
$ pip install -r requirements.txt
$ python time_complexity_tests.py
```

After this you should see a similar output to the example below, with the number of register and theirs runtimes, 
and also the line chart generated by matplotlib:


 Registers (array size) | Runtime(in seconds) |  Runtime/registers ( in seconds)
 ------------ | ------------ | -------------
  1000 | 0.020446395999897504 | 2.0446395999897503e-05  
 2000 | 0.040717989002587274 | 2.0358994501293637e-05  
 3000 | 0.08197243900212925 | 2.7324146334043083e-05  
 4000 | 0.1104673929985438 | 2.761684824963595e-05  
 5000 | 0.1382168210002419 | 2.764336420004838e-05  
 6000 | 0.16654095200283336 | 2.775682533380556e-05  
 7000 | 0.19386417599889683 | 2.769488228555669e-05  
 8000 | 0.21814606199768605 | 2.7268257749710756e-05  
 9000 | 0.2475190080003813 | 2.7502112000042367e-05  
 10000 | 0.27438658800019766 | 2.7438658800019766e-05  
 11000 | 0.304299796000123 | 2.7663617818193004e-05  
 12000 | 0.3309787120015244 | 2.7581559333460366e-05  
 13000 | 0.3593146399980469 | 2.7639587692157455e-05  
 14000 | 0.3843218260008143 | 2.7451559000058165e-05  
 15000 | 0.4107133910001721 | 2.7380892733344807e-05  
 16000 | 0.44137682400105405 | 2.758605150006588e-05  
 17000 | 0.4730835970003682 | 2.78284468823746e-05  
 18000 | 0.5046256390014605 | 2.8034757722303362e-05  
 19000 | 0.5301382789984928 | 2.7902014684131198e-05  
 20000 | 0.5503076480017626 | 2.751538240008813e-05  
 21000 | 0.5806114490005712 | 2.7648164238122438e-05  
 22000 | 0.610859464002715 | 2.776633927285068e-05  
 23000 | 0.6342663110008289 | 2.757679613047082e-05  
 24000 | 0.6607617449990357 | 2.753173937495982e-05  
 25000 | 0.7021272060010233 | 2.808508824004093e-05  
 26000 | 0.7175865289973444 | 2.7599481884513247e-05  
 27000 | 0.7399421320005786 | 2.7405264148169578e-05  
 28000 | 0.7757992289989488 | 2.7707115321391028e-05  
 29000 | 0.7975735410000198 | 2.7502535896552406e-05  
 30000 | 0.8340131269978883 | 2.7800437566596276e-05  
 31000 | 0.8626532910020615 | 2.782752551619553e-05  
 32000 | 0.886760923996917 | 2.7711278874903655e-05  
 33000 | 0.917001159999927 | 2.778791393939173e-05  
 34000 | 0.9373756319982931 | 2.756987152936156e-05  
 35000 | 0.9726722170016728 | 2.7790634771476366e-05  
 36000 | 0.997899748999771 | 2.771943747221586e-05  
 37000 | 1.0338467200017476 | 2.7941803243290477e-05  
 38000 | 1.0563124740001513 | 2.7797696684214508e-05  
 39000 | 1.08588795200194 | 2.7843280820562565e-05  
 40000 | 1.1073690470002475 | 2.7684226175006188e-05  





## Requirements:
- Python version >= 3.8.7
