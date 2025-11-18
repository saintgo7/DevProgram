class RestoreController < ApplicationController
  before_action :set_restore, only: [:show, :edit, :update, :destroy]

  # GET /restore
  def index
    @restores = Restore.all
    render json: @restores
  end

  # GET /restore/1
  def show
    render json: @restore
  end

  # POST /restore
  def create
    @restore = Restore.new(restore_params)

    if @restore.save
      render json: @restore, status: :created
    else
      render json: @restore.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /restore/1
  def update
    if @restore.update(restore_params)
      render json: @restore
    else
      render json: @restore.errors, status: :unprocessable_entity
    end
  end

  # DELETE /restore/1
  def destroy
    @restore.destroy
    head :no_content
  end

  private

  def set_restore
    @restore = Restore.find(params[:id])
  end

  def restore_params
    params.require(:restore).permit(:name)
  end
end
