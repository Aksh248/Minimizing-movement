
numBots = 50;               % Number of bots
connectivityRadius = 0.1;   % Connectivity radius
lineTransparency = 0.5;     % Transparency of the lines
moveDistance = 0.15;       % Distance to move each bot

% Create an empty matrix to store the bot positions
botPositions = zeros(numBots, 2);

figure;
hold on;

% Generating the initial bot positions randomly within the simulation area
botPositions(:, 1) = rand(numBots, 1);
botPositions(:, 2) = rand(numBots, 1);

% Plotting Robots as circles
for i = 1:numBots
    plot(botPositions(i, 1), botPositions(i, 2), 'o', 'MarkerSize', 5, 'MarkerFaceColor', 'b');
end

% Connecting the initial bots with line (forming clusters)
for i = 1:numBots
    for j = 1:numBots
        
        distance = norm(botPositions(i, :) - botPositions(j, :));
               
        if distance <= connectivityRadius
            line([botPositions(i, 1), botPositions(j, 1)], [botPositions(i, 2), botPositions(j, 2)], ...
                'Color', [0 0 1 lineTransparency]);
        end
    end
end

% Definig Simulation area
xlim([0 1]);
ylim([0 1]);


xlabel('X');
ylabel('Y');


title('Random Bot Connectivity Simulation')


% Define lineColor variable for detecting new lines to be made between new
% clusters
lineColor = nan(numBots,numBots);

pause(5)

% Check if the initial position is fully connected or not
fullyConnected = all(all(~isnan(lineColor)));
if fullyConnected
    disp('Network is already fully connected.')
else
    disp('Waiting for network to become fully connected...')
end

m = 1;

%disp(lineColor);
while any(isnan(lineColor(:)))

    %disp(m)
    lineColor = nan(numBots,numBots);

    % Create a new matrix to store the updated bot positions
    newBotPositions = zeros(numBots, 2);
    
    for i = 1:numBots
        %disp("for 1");
        % finding neghibor bot postion to know which bot to move and by how
        % much
        neighborIndices = find(norm(botPositions(i,:) - botPositions,2) >= connectivityRadius);
       
        neighborIndices = neighborIndices(neighborIndices ~= i);
        
        
        centroid = mean(botPositions(neighborIndices,:),1);
        
        
        direction = centroid - botPositions(i,:);
        
        
        moveDistanceThisBot = min(norm(direction,2), moveDistance);
        %disp(moveDistanceThisBot);
        
        % Update the new bot position with the new vector obtained
        newBotPositions(i,:) = botPositions(i,:) + moveDistanceThisBot * direction / norm(direction,2);
    end
    
    % Update the bot positions
    botPositions = newBotPositions;
    
    % Clear the old plot without removing the figure
    cla;
    markerSize = 5;
    lineWidth = 1;
        
    % Plotting new Robot position as circles
    for i = 1:numBots
        plot(botPositions(i, 1), botPositions(i, 2), 'o', 'MarkerSize', markerSize, 'MarkerFaceColor', 'g', 'MarkerEdgeColor', 'k');
        %disp('Plot circle for');
    end
    
    % Connecting the new bots with line (forming clusters)
    for i = 1:numBots
        for j = i+1:numBots
            
            distance = norm(botPositions(i, :) - botPositions(j, :));
            
            if distance <= connectivityRadius && isnan(lineColor(i,j))
                line([botPositions(i, 1), botPositions(j, 1)], [botPositions(i, 2), botPositions(j, 2)], ...
                    'Color', [0 0 1 lineTransparency], 'LineWidth', lineWidth);
                lineColor(i,j) = 1;
                lineColor(j,i) = 1;
                %disp('line for if');
            end
        end
    end
    %disp(lineColor);
    
   
    pause(10);
    %m = m+1;
    
end

