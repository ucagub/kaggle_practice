import numpy as np
from keras.layers import Input, Embedding, Reshape, Dot, Flatten
from keras.models import Model

class CFModel:
    def __init__(self, n_users, n_items, k_factors):
        # Define input layers for users and items
        user_input = Input(shape=(1,), name='user_input')
        item_input = Input(shape=(1,), name='item_input')

        # User embedding layer
        user_embedding = Embedding(input_dim=n_users, output_dim=k_factors, input_length=1)(user_input)
        user_vec = Flatten()(user_embedding)

        # Item embedding layer
        item_embedding = Embedding(input_dim=n_items, output_dim=k_factors, input_length=1)(item_input)
        item_vec = Flatten()(item_embedding)

        # Dot product of user and item vectors
        dot_product = Dot(axes=1)([user_vec, item_vec])

        # Define the model
        self.model = Model(inputs=[user_input, item_input], outputs=dot_product)
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    # The rate function to predict user's rating of unrated items
    def rate(self, user_id, item_id):
        return self.model.predict([np.array([user_id]), np.array([item_id])])[0][0]

# Example usage
# n_users = 1000  # Number of users
# n_items = 500  # Number of items
# k_factors = 50  # Number of latent factors
# cf_model = CFModel(n_users, n_items, k_factors)
