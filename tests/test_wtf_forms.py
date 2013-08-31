import unittest

from schematics.models import Model
from schematics.types.base import *
from schematics_wtf.converter import model_form

from pprint import pprint

class Test(Model):
  pk = StringType(required=True)
  name = StringType()
  age = IntType()
  country = StringType(default='US', choices=['US','UK'])

class TestWTForms(unittest.TestCase):

  def testMakeForm(self):
    f = model_form(Test())
    myform = f()
    assert 'pk' in myform
    assert 'name' in myform
    assert 'age' in myform
    assert 'required' in  myform.pk.flags

  def testModelFormOnly(self):
    f = model_form(Test(), only=['name', 'age'])
    myform = f()
    assert 'pk' not in myform
    assert 'name' in myform
    assert 'age' in myform
    assert 'time' not in myform
    
  def testModelFormExclude(self):
    f = model_form(Test(), exclude=['pk'])
    myform = f()
    assert 'pk' not in myform
    assert 'name' in myform
    assert 'age' in myform
    
  def testModelFormHidden(self):
    f = model_form(Test(), hidden=['pk'])
    myform = f()
    assert 'hidden' in unicode(myform.pk)
    
  def testModelFormWithData(self):
    m = Test(dict(name="Dude",age=35,pk="saweet"))
    f = model_form(m)
    myform = f()
    assert 'Dude' in unicode(myform.name) 
    assert '35' in unicode(myform.age)
    assert 'saweet' in unicode(myform.pk)
    assert myform.validate()

  def testModelFormWithDataAndHiddenFields(self):
    m = Test(dict(name="Dude",age=35,pk="saweet"))
    f = model_form(m, hidden=['pk'])
    myform = f()
    assert 'hidden' in unicode(myform.pk)
    assert 'Dude' in unicode(myform.name) 
    assert '35' in unicode(myform.age)
    assert 'saweet' in unicode(myform.pk)
    assert myform.validate()

if __name__ == "__main__":  
  unittest.main()
