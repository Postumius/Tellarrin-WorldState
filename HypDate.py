dayNames = ['Silth', 'Est', 'Kross', 'Oust', 'Rest', 'Streth', 
            'Eith', 'Kesh', 'Orseh', 'Rath']


class HypDate:

    def __init__(
    self, 
    year=0, 
    season=0, 
    cycle=0, 
    day=0, 
    hour=0, 
    minute=0):
        self.year = year
        self.season = season 
        self.cycle = cycle
        self.day = day
        self.hour = hour
        self.minute = minute
    
    def plus(self, other):
        def multiBaseAddition(xs, ys, bs):
            def tail(ls):
                cp = ls.copy()
                cp.pop(0)
                return cp

            if len(bs) == 0:
                return [ xs[0] + ys[0] ]
            else:
                rest = multiBaseAddition(
                    tail(xs), tail(ys), tail(bs))
                return [
                    xs[0] + ys[0] + rest[0] // bs[0],
                    rest[0] % bs[0]
                ] + tail(rest)

        return HypDate.fromList(multiBaseAddition(
            self.toList(),
            other.toList(),
            [4, 9, 10, 24, 60]
        ))
    
    def toList(self): 
        return [self.year, self.season, self.cycle, self.day,
            self.hour, self.minute]

    @staticmethod
    def fromList(ls):        
        return HypDate(ls[0], ls[1], ls[2], ls[3], ls[4], ls[5])

    def seasonName(self):
        return['Seed', 'Harvest', 'Scorch', 'Frost'][self.season]

    def cycleName(self):
        return {
            0 : '1st',
            1 : '2nd',
            2 : '3rd'
        }.get(self.cycle, str(self.cycle + 1) + 'th')

    def dayName(self):
        return dayNames[self.day]

    def dateName(self):
        return '{} {} of {}, {} YoR'.format(
            self.cycleName(), self.dayName(), 
            self.seasonName(), str(self.year))

    def timeName(self):
        return '{}:{}'.format(
            str(self.hour).zfill(2),
            str(self.minute).zfill(2)
        )
        

    
