class HashingController < ApplicationController
  before_action :set_hashing, only: [:show, :edit, :update, :destroy]

  # GET /hashing
  def index
    @hashings = Hashing.all
    render json: @hashings
  end

  # GET /hashing/1
  def show
    render json: @hashing
  end

  # POST /hashing
  def create
    @hashing = Hashing.new(hashing_params)

    if @hashing.save
      render json: @hashing, status: :created
    else
      render json: @hashing.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /hashing/1
  def update
    if @hashing.update(hashing_params)
      render json: @hashing
    else
      render json: @hashing.errors, status: :unprocessable_entity
    end
  end

  # DELETE /hashing/1
  def destroy
    @hashing.destroy
    head :no_content
  end

  private

  def set_hashing
    @hashing = Hashing.find(params[:id])
  end

  def hashing_params
    params.require(:hashing).permit(:name)
  end
end
