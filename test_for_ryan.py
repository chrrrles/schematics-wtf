from schematics.models import Model
from schematics.types.base import *
from schematics.types.compound import *
from schematics_wtf.converter import model_form

class Test(Model):
  pk = StringType(required=True, max_length=30)
  name = StringType(max_length=30)
  age = IntType()
  country = StringType(default='US', choices=['US','UK'])

class ModelTypeTest(Model):
  name = StringType(required=True,max_length=30)
  child = ModelType(Test)

def testModelFormWithModelType():
  m = ModelTypeTest({
    'name' : "Lebowski",
    'child' : {'name':"Dude", 'age':35, 'pk':"saweet"}})

  print "model name:  %s" % m.name
  print "child model age:  %s" % m.child.age
  f = model_form(m)
  myform = f()
  print "form name html: %s" %myform.name 
  print "child form age html: %s" % myform.child.age
  assert "Lebowski" in unicode(myform.name)

if __name__ == "__main__":
  testModelFormWithModelType()

