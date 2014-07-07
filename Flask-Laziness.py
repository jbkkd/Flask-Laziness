class_name = raw_input("Enter class name:")
input_data = raw_input("Enter class vals:")
class_variables = input_data.split()

# class definition
print "class " + class_name + "(db.Model):"
print '    """\n    This model \n    """\n'
print "    id = db.Column(db.Integer(), primary_key=True)"
print "    _date = db.Column(\"date\", db.DateTime())"
for i in class_variables:
    print "    _" + i + " = db.Colomun(\"" + i + "\", db)"
print "    _admin_notes = db.Column(\"admin_notes\", db.Text())"



# init definition
print ""
print "    def __init__(self, date,",
for i in class_variables:
    print i + ",",
print "admin_notes):"
print "         self.date = date"
for i in class_variables:
    print "        self." + i + " = " + i
print "        self.admin_notes = admin_notes"

# reper
print ""
print "    def __repr__(self):"
print "        return '< " + class_name + " %s >' % self.id"

# property definition
print ""
print """    @hybrid_property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value\n"""

for i in class_variables:
    print """    @hybrid_property
    def %s(self):
        return self._%s

    @%s.setter
    def %s(self, value):
        self._%s = value\n""" % (i, i, i, i, i,)

print ""
print """    @hybrid_property
    def admin_notes(self):
        return self._admin_notes

    @admin_notes.setter
    def admin_notes(self, value):
        self._admin_notes = value\n"""
class_name = raw_input("Press Enter to exit.")


