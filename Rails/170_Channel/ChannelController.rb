class ChannelController < ApplicationController
  before_action :set_channel, only: [:show, :edit, :update, :destroy]

  # GET /channel
  def index
    @channels = Channel.all
    render json: @channels
  end

  # GET /channel/1
  def show
    render json: @channel
  end

  # POST /channel
  def create
    @channel = Channel.new(channel_params)

    if @channel.save
      render json: @channel, status: :created
    else
      render json: @channel.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /channel/1
  def update
    if @channel.update(channel_params)
      render json: @channel
    else
      render json: @channel.errors, status: :unprocessable_entity
    end
  end

  # DELETE /channel/1
  def destroy
    @channel.destroy
    head :no_content
  end

  private

  def set_channel
    @channel = Channel.find(params[:id])
  end

  def channel_params
    params.require(:channel).permit(:name)
  end
end
