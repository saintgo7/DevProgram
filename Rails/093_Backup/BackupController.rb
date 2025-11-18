class BackupController < ApplicationController
  before_action :set_backup, only: [:show, :edit, :update, :destroy]

  # GET /backup
  def index
    @backups = Backup.all
    render json: @backups
  end

  # GET /backup/1
  def show
    render json: @backup
  end

  # POST /backup
  def create
    @backup = Backup.new(backup_params)

    if @backup.save
      render json: @backup, status: :created
    else
      render json: @backup.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /backup/1
  def update
    if @backup.update(backup_params)
      render json: @backup
    else
      render json: @backup.errors, status: :unprocessable_entity
    end
  end

  # DELETE /backup/1
  def destroy
    @backup.destroy
    head :no_content
  end

  private

  def set_backup
    @backup = Backup.find(params[:id])
  end

  def backup_params
    params.require(:backup).permit(:name)
  end
end
