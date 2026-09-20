class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = students
        rejections = 0
        while students_queue and rejections < len(students_queue):
            if students_queue[0] == sandwiches[0]:
                students_queue.pop(0)
                sandwiches.pop(0)
                rejections = 0
            else:
                moved_student = students_queue[0]
                students_queue.pop(0)
                students_queue.append(moved_student)
                rejections += 1
        return len(students_queue)
                
                