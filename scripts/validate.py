import logging

logger = logging.getLogger(__name__)


def test_data(df, tests):
    """
    Run provided data tests on provided data.
    Parameters
    ----------
    df : pandas.DataFrame object
      The dataset to test.
    tests : dict
      A mapping from tests to failure messages.
    
    Returns
    ----------
    boolean
    """
    logger.info('Starting validate.test_data method')
    print('***** df head() **********************')
    print(df.head())
    print(tests)

    results = []
    for test_func, failure_message in tests:
        results.append(test_func(df.copy()))
        if results[-1]:
            logger.info(f'Data test {test_func.__name__} passed.')
        else:
            logger.error(f'Data test {test_func.__name__} failed. {failure_message}')
    logger.info(f'{sum(results)}/{len(results)} passed.')
    ans = sum(results) == len(results)
    print('ans is ', ans)
    return ans


def cases_vs_deaths(df):
    """Checks that death count is no more than case count."""
    logger.info('Starting validate.cases_vs_deaths method')
    print('***** df head() **********************')
    print(df.head())

    result = (df['deaths'] <= df['cases']).all()
    print(result)
    return result


def unique_records(df):
    """Checks that each date and FIPs combination is unique."""
    logger.info('Starting validate.unique_records method')
    print('***** df head() **********************')
    print(df.head())

    result = df[['date', 'fips']].drop_duplicates().shape[0] == df.shape[0]
    print(result)
    return result


def no_nulls_test(df):
    """Checks that all elements are not null"""
    logger.info('Starting validate.no_nulls_test method')
    print('***** df head() **********************')
    print(df.head())

    result = df.isnull().values.sum() == 0
    print(result)
    return result


def range_test(series, min, max):
    """Checks that all values in a series are within a range, inclusive"""
    logger.info('Starting validate.range_test method')
    print('***** df head() **********************')
    print('series is ', series)
    print('min is ', min)
    print('max is ', max)

    result = (series >= min).all() and (series <= max).all() 
    print(result)
    return result


def cases_range_test(df):
    """Checks that all cases are non-negative and <= 10M"""
    logger.info('Starting validate.cases_range_test method')
    print('***** df head() **********************')
    print(df.head())

    result = range_test(df['cases'], 0, 10e6)
    print(result)
    return result



def deaths_range_test(df):
    """Checks that all deaths are non-negative and <= 100K"""
    logger.info('Starting validate.cases_range_test method')
    print('***** df head() **********************')
    print(df.head())

    result = range_test(df['deaths'], 0, 1e5)
    print(result)
    return result


# Data test for NYT covid cases and deaths
nyt_cases_counties = [
    (cases_vs_deaths, "Death counts cannot exceed case counts."),
    (unique_records, "Only one record per FIPs, per date allowed."),
    (no_nulls_test, "All values are expected to be non-null."),
    (cases_range_test, "Cases must be non-negative and <= 10M."),
    (deaths_range_test, "Deaths must be non-negative and <= 100K.")
]

