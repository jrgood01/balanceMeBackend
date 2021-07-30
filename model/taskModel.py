class task():
    def __init__(self, cursor, id='',name='', point_value='', category_id='', estimated_time='', description='', start_time='',
                estimated_completion_time='', status='', completion_time='', image_path='', assigned_user_id=-1,
                created_user_id=-1,history='',repeat='',completed='',active=1,steps=''):
        self.id = id
        self.name = name
        self.point_value = point_value
        self.category_id = category_id 
        self.estimated_time = estimated_time
        self.description = description
        self.start_time = start_time
        self.estimated_completion_time = estimated_completion_time
        self.status = status
        self.completion_time = completion_time
        self.image_path = image_path
        self.assigned_user_id = assigned_user_id
        self.created_user_id = created_user_id
        self.history = history
        self.repeat = repeat
        self.completed = completed
        self.active = active
        self.steps = steps
        self.cursor = cursor
    def createTask(self):
        if self.start_time != None:
            sql = ("INSERT INTO tasks "
                "(name, point_value, category_id, estimate_time, description, start_time, estimated_completion_time, status, image_path, assigned_user_id, created_user_id)"
                "VALUES ('%s', %d, %d, '%s', '%s', '%s', '%s', %d, '%s', %d, %d)" % 
                (self.name, self.point_value, self.category_id, self.estimated_time, 
                self.description, self.start_time, self.estimated_completion_time, 
                self.status, self.image_path, self.assigned_user_id, self.created_user_id))
        self.cursor.execute(sql)
        return 
    def dict():
        return {'name' : self.name,
                'point_value' : self.point_value,
                'category_id' : self.category_id,
                'estimated_time' : self.estimated_time,
                'description' : self.description,
                'start_time' : self.start_time,
                'estimated_completion_time' : self.estimated_completion_time,
                'status' : self.status,
                'image_path' : self.image_path,
                'assigned_user_id' : self.assigned_user_id,
                'created_user_id' : self.created_user_id}