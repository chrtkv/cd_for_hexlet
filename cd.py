#! /usr/bin/env python3

# Change directory based on url

import sys
import os


def get_path(url):
    parent = "/home/kirill/hexlet-exercise-kit"

    if 'challenges' in url:
        return '{}/challenges/'.format(parent)

    course_name = url.split('/')[4].replace('-', '_')

    if 'courses' in url and 'exercise_unit' not in url:
        return '{}/courses-ru/{}_course'.format(parent, course_name)

    lesson_name = url.split('/')[6].replace('-', '_')

    if 'exercise_unit' in url:
        return '{}/courses/course-{}/{}_{}_exercise/'.format(
            parent, url.split('/')[4], course_name, lesson_name)

    return parent


def main(url):
    os.chdir(get_path(url))
    os.system("/bin/bash")


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
