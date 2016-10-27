 def _convertToOneOfMany(self, bounds=(0, 1)):
        """Converts the target classes to a 1-of-k representation, retaining the
        old targets as a field `class`.
        To supply specific bounds, set the `bounds` parameter, which consists of
        target values for non-membership and membership."""
        if self.outdim != 1:
            # we already have the correct representation (hopefully...)
            return
        if self.nClasses <= 0:
            self.calculateStatistics()
        oldtarg = self.getField('target')
        newtarg = zeros([len(self), self.nClasses], dtype='Int32') + bounds[0]
        for i in range(len(self)):
            newtarg[i, int(oldtarg[i])] = bounds[1]
        self.setField('target', newtarg)
        self.setField('class', oldtarg)
        # probably better not to link field, otherwise there may be confusion
        # if getLinked() is called?
        ##self.linkFields(self.link.append('class'))
