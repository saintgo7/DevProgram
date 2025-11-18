class MigrationController < ApplicationController
  before_action :set_migration, only: [:show, :edit, :update, :destroy]

  # GET /migration
  def index
    @migrations = Migration.all
    render json: @migrations
  end

  # GET /migration/1
  def show
    render json: @migration
  end

  # POST /migration
  def create
    @migration = Migration.new(migration_params)

    if @migration.save
      render json: @migration, status: :created
    else
      render json: @migration.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /migration/1
  def update
    if @migration.update(migration_params)
      render json: @migration
    else
      render json: @migration.errors, status: :unprocessable_entity
    end
  end

  # DELETE /migration/1
  def destroy
    @migration.destroy
    head :no_content
  end

  private

  def set_migration
    @migration = Migration.find(params[:id])
  end

  def migration_params
    params.require(:migration).permit(:name)
  end
end
