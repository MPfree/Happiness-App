

def indicator_averages(days):
    num_days = len(days)
    if num_days>0:
        indicator_names=list(days[0].keys())

        indicator_averages = {}
        
        for i in range(len(indicator_names)):
            indicator_averages[indicator_names[i]] = 0

        num_indicators = len(days[0])

        for i in range(num_days):
            day = days[i]
            for indicator in day:
                indicator_averages[indicator] += day[indicator]

        for indicator in indicator_averages:
            indicator_averages[indicator] = (indicator_averages[indicator]) / num_days

        return indicator_averages
    
    else:
        return {}