class TeamController < ApplicationController
  before_action :set_team, only: [:show, :edit, :update, :destroy]

  # GET /team
  def index
    @teams = Team.all
    render json: @teams
  end

  # GET /team/1
  def show
    render json: @team
  end

  # POST /team
  def create
    @team = Team.new(team_params)

    if @team.save
      render json: @team, status: :created
    else
      render json: @team.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /team/1
  def update
    if @team.update(team_params)
      render json: @team
    else
      render json: @team.errors, status: :unprocessable_entity
    end
  end

  # DELETE /team/1
  def destroy
    @team.destroy
    head :no_content
  end

  private

  def set_team
    @team = Team.find(params[:id])
  end

  def team_params
    params.require(:team).permit(:name)
  end
end
