class PusherController < ApplicationController
  before_action :set_pusher, only: [:show, :edit, :update, :destroy]

  # GET /pusher
  def index
    @pushers = Pusher.all
    render json: @pushers
  end

  # GET /pusher/1
  def show
    render json: @pusher
  end

  # POST /pusher
  def create
    @pusher = Pusher.new(pusher_params)

    if @pusher.save
      render json: @pusher, status: :created
    else
      render json: @pusher.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /pusher/1
  def update
    if @pusher.update(pusher_params)
      render json: @pusher
    else
      render json: @pusher.errors, status: :unprocessable_entity
    end
  end

  # DELETE /pusher/1
  def destroy
    @pusher.destroy
    head :no_content
  end

  private

  def set_pusher
    @pusher = Pusher.find(params[:id])
  end

  def pusher_params
    params.require(:pusher).permit(:name)
  end
end
