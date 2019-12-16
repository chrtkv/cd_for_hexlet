#! /usr/bin/env python3

# Change directory based on url

import sys
import os


def get_path(url):
    parent = "/home/kirill/hexlet-exercise-kit"

    course_name = url.split('/')[4]
    course_name_underscore = course_name.replace('-', '_')

    if 'challenges' in url:
        def find_dir(challenge_name):
            challenges_dirs = os.listdir('{}/challenges'.format(parent))
            challenge_name_dash = challenge_name.replace('_', '-')
            dir_name = 'challenge-{}'.format(challenge_name_dash)
            if dir_name in challenges_dirs:
                return dir_name
            return find_dir(challenge_name.rsplit('_', 1)[0])

        challenge_dir = find_dir(course_name)

        return '{}/challenges/{}/{}_challenge'.format(
            parent, challenge_dir, course_name_underscore)

    if 'courses' in url and 'exercise_unit' not in url:
        return '{}/courses-ru/{}_course'.format(parent, course_name_underscore)

    lesson_name = url.split('/')[6].replace('-', '_')

    if 'exercise_unit' in url:
        return '{}/courses/course-{}/{}_{}_exercise/'.format(
            parent, url.split('/')[4], course_name_underscore, lesson_name)

    return parent


def main(url):
    os.chdir(get_path(url))
    os.system("/bin/bash")


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
