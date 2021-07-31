def get_page_list(current_page, page_count, button_count):
        if page_count <= button_count:
            return list( range(1, page_count+1) )
        else:
            start = current_page - button_count // 2
            end = current_page + button_count // 2
            print(start, end)
            if start < 1:
                end += 1 - start
                start = 1
            elif end > page_count:
                start -= end - page_count
                end = page_count
            return list( range(start, end+1) )[:page_count]