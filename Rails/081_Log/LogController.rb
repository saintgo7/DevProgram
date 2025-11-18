class LogController < ApplicationController
  before_action :set_log, only: [:show, :edit, :update, :destroy]

  # GET /log
  def index
    @logs = Log.all
    render json: @logs
  end

  # GET /log/1
  def show
    render json: @log
  end

  # POST /log
  def create
    @log = Log.new(log_params)

    if @log.save
      render json: @log, status: :created
    else
      render json: @log.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /log/1
  def update
    if @log.update(log_params)
      render json: @log
    else
      render json: @log.errors, status: :unprocessable_entity
    end
  end

  # DELETE /log/1
  def destroy
    @log.destroy
    head :no_content
  end

  private

  def set_log
    @log = Log.find(params[:id])
  end

  def log_params
    params.require(:log).permit(:name)
  end
end
