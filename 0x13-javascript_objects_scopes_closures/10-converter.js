#!/usr/bin/node

exports.converter = function (base) {
  function myConv (n) {
    return n.toString(base);
  }
  return myConv;
};
