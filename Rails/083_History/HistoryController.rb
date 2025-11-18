class HistoryController < ApplicationController
  before_action :set_history, only: [:show, :edit, :update, :destroy]

  # GET /history
  def index
    @historys = History.all
    render json: @historys
  end

  # GET /history/1
  def show
    render json: @history
  end

  # POST /history
  def create
    @history = History.new(history_params)

    if @history.save
      render json: @history, status: :created
    else
      render json: @history.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /history/1
  def update
    if @history.update(history_params)
      render json: @history
    else
      render json: @history.errors, status: :unprocessable_entity
    end
  end

  # DELETE /history/1
  def destroy
    @history.destroy
    head :no_content
  end

  private

  def set_history
    @history = History.find(params[:id])
  end

  def history_params
    params.require(:history).permit(:name)
  end
end
