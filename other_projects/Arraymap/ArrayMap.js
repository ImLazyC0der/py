function arraymap(){
  const arry=[1,2,3,4,5];
 const newArr=arry.map(function(val,index,arry)
 {
   return val+5;
 });
 console.log("Original Array=",arry);
 console.log("After Mapping=",newArr);
  }
 
  arraymap();

  // To run this code use node ArrayMap.js in gitbash
