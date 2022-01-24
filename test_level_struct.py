# These are files for pytest testing only.
import main_lint


def test_level_valid():
    # give a valid rawlevel and expect the class contents to match
    rawfile = main_lint.loc_levels('test_1.txt')
    rawfile = main_lint.proc_file(rawfile)
    levels = main_lint.assemble_level_list(rawfile)

    assert levels[0].name == 'Time to explore'
    assert levels[0].us_lines_count == '06'
    assert levels[0].us_nesc_deaths == '000002'
    assert levels[0].nesc_deaths == 2
    assert levels[0].width == 32
    assert levels[2].blockmode == 'L'
    assert levels[1].ent_num == 1
    assert levels[2].nesc_deaths == 0


if __name__ == '__main__':
    test_level_valid()
