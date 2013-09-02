import unittest

from schematics.models import Model
from schematics.types.base import *
from schematics.types.compound import *
from schematics_wtf.converter import model_form

from pprint import pprint

class Test(Model):
  pk = StringType(required=True)
  name = StringType()
  age = IntType()
  country = StringType(default='US', choices=['US','UK'])

class TestWithMaxLength(Model):
  pk = StringType(required=True, max_length=30)
  name = StringType(max_length=30)
  age = IntType()
  country = StringType(default='US', choices=['US','UK'])

class ModelTypeTest(Model):
  name = StringType(required=True)
  child = ModelType(Test)

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

  def testModelFormWithMaxLength(self):
    m = TestWithMaxLength(dict(name="Dude",age=35,pk="saweet"))
    f = model_form(m)
    myform = f()
    assert 'Dude' in unicode(myform.name) 
    assert 'type="text"' in unicode(myform.name) 
    assert '35' in unicode(myform.age)
    assert 'saweet' in unicode(myform.pk)
    assert myform.validate()

  def testModelFormWithModelType(self):
    m = ModelTypeTest({
      'name' : "Lebowski",
      'child' : {'name':"Dude", 'age':35, 'pk':"saweet"}})

    f = model_form(m)
    myform = f()

    assert 'Lebowski' in unicode(myform.name)
    assert 'Dude' in unicode(myform.child.name)
    assert '35' in unicode(myform.child.age)
    assert 'saweet' in unicode(myform.child.pk)
    assert myform.validate()

if __name__ == "__main__":  
  unittest.main()
