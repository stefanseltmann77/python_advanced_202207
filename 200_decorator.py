def transaction(dbfunction):
    """Decorator for wrapping a call into an transaction"""
    def func_call(self, *args, **kwargs):
        self.db.query("BEGIN")
        dbfunction(self, *args, **kwargs)
        if self.debug_mode:
            self.db.query("ROLLBACK")
        else:
            self.db.query("COMMIT")
    return func_call


class DataBaseFunctions(object):

    @transaction
    def mess_up_important_tables(self, inputs):
        ############# do queries
        pass

    def mess_up_important_tables_wo_decorator(self, inputs):
        self.db.query("BEGIN")
        ############# do queries
        if self.debug_mode:
            self.db.query("ROLLBACK")
        else:
            self.db.query("COMMIT")
