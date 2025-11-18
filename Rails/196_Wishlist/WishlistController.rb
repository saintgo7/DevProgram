class WishlistController < ApplicationController
  before_action :set_wishlist, only: [:show, :edit, :update, :destroy]

  # GET /wishlist
  def index
    @wishlists = Wishlist.all
    render json: @wishlists
  end

  # GET /wishlist/1
  def show
    render json: @wishlist
  end

  # POST /wishlist
  def create
    @wishlist = Wishlist.new(wishlist_params)

    if @wishlist.save
      render json: @wishlist, status: :created
    else
      render json: @wishlist.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /wishlist/1
  def update
    if @wishlist.update(wishlist_params)
      render json: @wishlist
    else
      render json: @wishlist.errors, status: :unprocessable_entity
    end
  end

  # DELETE /wishlist/1
  def destroy
    @wishlist.destroy
    head :no_content
  end

  private

  def set_wishlist
    @wishlist = Wishlist.find(params[:id])
  end

  def wishlist_params
    params.require(:wishlist).permit(:name)
  end
end
